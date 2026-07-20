


def found_a_number( model,np,prompt, function, parameter) -> None:

        prompt_t = f"""
            You are extracting function parameters.

            Rules:
            - Do NOT solve the user's request.
            - Return only the value of the requested parameter.
            - If the user asks for a square root, return the original input number, not the square root.
            - Keep negative numbers and decimal numbers exactly as they appear.

            Example:
            User request: What is the sum of -5 and 8?
            fn_add_numbers(a = -5, b = 8)

            User request: Calculate the square root of 300
            Function: fn_get_square_root(a = 300)

            Now complete this:

            User request: {prompt}
            Function: {function}({parameter}=
            """
        # print(prompt_t)
        prompt_ids =  model.encode(prompt_t).squeeze().tolist()
        result = []
       
        digits = [model.encode(str(i)).squeeze().tolist() for i in range(10)]
        dot = model.encode('.').squeeze().tolist()
        sign = model.encode('-').squeeze().tolist()
        comma = model.encode(",").squeeze().tolist()

        allowed_ids = []
        # print(model.encode('3').squeeze().tolist())
        for s in range(10):
            logits  = model.get_logits_from_input_ids(prompt_ids + result)

            masked = np.full_like(logits, -np.inf)
            
            if len(result) == 0:
                allowed_ids = digits + [sign]
            else:
                allowed_ids = digits + [dot, comma]

            for  i in allowed_ids:
                masked[i] = logits[i]
            
            max_id = np.argmax(masked)
            
            if max_id == comma:
                break

            result.append(max_id)
           

        return (model.decode(result))


def  found_a_string_param(model,np,function, prompt, parameter) -> None:

    # if parameter == "regex":
    prompt_t = f"""
    You are extracting the regular expression for a function call.

    Rules:
    - Return ONLY the value of the requested parameter.
    - Do not explain.
    - Do not return the function call.
    - Do not return any other parameters.
    - Do not add extra text.

    Examples:
    User request:
    Replace all numbers in "abc123" with NUM  
    fn_substitute_string_regex(source_string="abc123",regex="[0-9]" ,replacement = "NUM")

    User request:
    {prompt}
    {function}({parameter}="
    """
#     else:
#         prompt_t = f"""
# -> User request:
# {prompt}
# {function}({parameter}="
# """

    prompt_ids = model.encode(prompt_t).squeeze().tolist()
    result = []
    re_text = ""
    for _ in range(20):
        logits = model.get_logits_from_input_ids(prompt_ids + result)

        max_id = np.argmax(logits)
        result.append(max_id)

        re_text += model.decode(max_id)
        if '"' in re_text:
            break

    return (re_text).split('"')[0]
