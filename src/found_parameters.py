


def found_a_number( model,np,prompt, function, parameter) -> None:

        prompt_t = f"""
            -> User request: {prompt}
            {function}({parameter}=
            """
        print(prompt_t)
        prompt_ids =  model.encode(prompt_t).squeeze().tolist()
        result = []
       
        allowed_ids = [model.encode(str(i)).squeeze().tolist() for i in range(10)]
        comma = model.encode(",").squeeze().tolist()
        allowed_ids.append(comma)
        for _ in range(10):
            logits  = model.get_logits_from_input_ids(prompt_ids + result)

            masked = np.full_like(logits, -np.inf)

            for  i in allowed_ids:
                masked[i] = logits[i]
            
            max_id = np.argmax(masked)
            if max_id == comma:
                break

            result.append(max_id)

        return(model.decode(result))






def  found_a_string_param(model,np,function, prompt, parameter) -> None:
    prompt_t = f"""
    Example 1

    User :
    Reverse the string 'abc'

    Function:
    fn_reverse_string

    Parameter:
    text='abc'

    Example 2

    User :
    Reverse the string 'OpenAI'

    Function:
    fn_reverse_string

    Parameter:
    text='OpenAI'

    Solve it:

    User:
    {prompt}

    Function:
    {function}

    Parameter:
    {parameter}='
    """

    stop = model.encode('"').squeeze().item()
    stop_t = model.encode("'").squeeze().item()
    prompt_ids = model.encode(prompt_t).squeeze().tolist()
    result = []
    re_text = ""
    for _ in range(20):
        logits = model.get_logits_from_input_ids(prompt_ids + result)

        max_id = np.argmax(logits)
       
        if max_id == stop or max_id == stop_t:
            print("hna")
            break
        result.append(max_id)

        re_text += model.decode([max_id])

    return (re_text)


# def  found_a_string_param(model,np,function, prompt, parameter) -> None:
#     prompt_t = f"""
#         -> User request: {prompt}
#         {function}({parameter}=
#         """
#     stop = model.encode('"').squeeze().tolist()
#     prompt_ids = model.encode(prompt_t).squeeze().tolist()
#     result = []

#     for _ in range(20):
#         logits = model.get_logits_from_input_ids(prompt_ids + result)

#         max_id = np.argmax(logits)
#         if max_id == stop:
#             break
#         result.append(max_id)
#     print("hna",model.decode(result))
#     return (model.decode(result))
