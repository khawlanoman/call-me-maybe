


def found_a_number( model,np,prompt, function, parameter) -> None:

        prompt_t = f'''
    #-> {prompt}
{function}({parameter}='''

        prompt_ids =  model.encode(prompt_t).squeeze().tolist()
        result = []

        digits = [model.encode(str(i)).squeeze().tolist() for i in range(10)]
        dot = model.encode('.').squeeze().tolist()
        sign = model.encode('-').squeeze().tolist()
        comma = model.encode(",").squeeze().tolist()

        allowed_ids = []

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


def  found_a_string_param(model,np,function, prompt, parameter, k) -> None:

    prompt_t = f'''
-> {prompt}
{function}({parameter}="'''

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

    result = (re_text).split('"')[0]

    return result.strip('\n')
