import numpy as np
from typing import Any


def llm_prompt(prompts: list) -> list:
    prompt_list = []
    for prompt in prompts:
        prompt_text = prompt.prompt

        f_prompt = f"{prompt_text}"
        prompt_list.append(f_prompt)

    return (prompt_list)


def function_token_ids(functions: list, model: Any,
                       not_found_function: Any) -> list:

    all_functions = []
    for v in functions:
        all_functions.append(model.encode(v.name).squeeze().tolist())
    all_functions.append(model.encode(not_found_function["name"]).squeeze().tolist()) # noqa
    return (all_functions)


def convet(prompt: str, list_functions: list, functions: Any,
           model: Any, not_found_function: Any) -> str | None:

    functions_dict = {
        fn.name: fn.description for fn in functions
    }

    functions_dict[not_found_function["name"]] = not_found_function["description"] # noqa

    full_prompt = f"""
    You are a function selection agent.

    Your task is to analyze the user's request and
    determine which available function is the best match.

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
    functions_text = model.decode(list_functions)
    functions_text.append('"')
    prompt_ids = model.encode(full_prompt).squeeze().tolist()
    result: list[Any] = []
    for _ in range(30):
        logits = model.get_logits_from_input_ids(prompt_ids + result)

        masked = np.full_like(logits, -np.inf)

        if result:
            t_functions = [fn for fn in list_functions
                           if fn[:len(result)] == result]
        else:
            t_functions = list_functions
        for v in t_functions:
            for tkid in v:
                masked[tkid] = logits[tkid]
        cor = np.argmax(masked)
        result.append(cor)

        result_txt = model.decode(result)

        if result_txt in functions_text:
            return (f"{result_txt}")

    return None
