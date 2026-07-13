from llm_sdk.llm_sdk import Small_LLM_Model
import numpy as np

def llm_prompt(prompts: list) -> None:
    prompt_list = []
    for prompt in  prompts:
        prompt_text = prompt.prompt

        f_prompt = f"{prompt_text}"

                # print(f"- {param_name}: {param.type}")
        prompt_list.append(f_prompt)

    return (prompt_list)

def function_token_ids(functions: list, model) -> None:
   
    all_functions = []
    for v in functions:
        all_functions.append(model.encode(v.name).squeeze().tolist())
    return(all_functions)


def convet(prompt, list_functions, functions, model) -> str:

    functions_dict = {
        fn.name: fn.description for fn in functions
    }
   
    full_prompt = f"""
    You are a function selection agent.

    Your task is to analyze the user's request and determine which available function is the best match.

    User request:
    {prompt}

    Available functions:
    {functions_dict}

    Rules:
    - Select exactly ONE function.
    - Return ONLY the function name.
    - Do NOT explain your reasoning.
    - Do NOT generate code.
    - Do NOT return JSON.
    - Do NOT include quotes, markdown, or additional text.
    - If no function matches the request, return:
    NONE

    Examples:

    User:
    What is the sum of 2 and 3?

    Output:
    fn_add_numbers

    User:
    Translate "Hello" to French.

    Output:
    fn_translate

    User:
    What's the weather in Paris?

    Output:
    fn_get_weather

    User:
    Tell me a joke.

    Output:
    NONE

    Now determine the best function for the user's request.

    Output:
    """
    functions_text =  model.decode(list_functions)
    functions_text.append('"')
    prompt_ids = model.encode(full_prompt).squeeze().tolist()
    result = []
    for _ in range(30):
        logits = model.get_logits_from_input_ids(prompt_ids + result)
        
        masked = np.full_like(logits, -np.inf)

        for v in list_functions:
            for tkid in v:
                masked[tkid] = logits[tkid]
        cor = np.argmax(masked)
        result.append(cor)
        result_txt = model.decode(result)
        if result_txt in functions_text:
            return result_txt
