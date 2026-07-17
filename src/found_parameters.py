


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