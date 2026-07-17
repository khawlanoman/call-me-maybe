def found_a_number( model,np,prompt, function) -> None:

    prompt_t = f"""
        User request:
        {prompt}

        Available function:
        {function}

         Rules:
        - Select exactly ONE parameter.
        - Return ONLY the parameter.

         Examples:

        User:
        What is the sum of 2 and 3?

        parameter:
        a

        Output:
        2

        User:
        What is the sum of 2 and 3?

        parameter:
        b

        Output:
        3
    """

    prompt_ids =  model.encode(prompt_t).squeeze().tolist()
    result = []
    digits = [
        "0", "1","2","3","4","5",
        "6","7","8","9"
    ]
    digits_ids = []
    for i in digits:
        digits_ids.append(model.encode(i).squeeze().tolist())
    
    for _ in range(10):
        logits  = model.get_logits_from_input_ids(prompt_ids + result)

        masked = np.full_like(logits, -np.inf)

        for  i in digits:
            masked[i] = logits[i]
        
        max_id = np.argmax(masked)
        result.append(max_id)

        result_text = model.decode(resulr)
        if result_text in digits_ids:
            return result_text
    