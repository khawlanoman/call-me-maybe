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

def function_token_ids(functions: list) -> None:
    model = Small_LLM_Model()
    all_functions = []
    for v in functions:
        all_functions.append(model.encode(v.name).squeeze().tolist())
    return(all_functions)


def convet(prompts_list, list_functions) -> str:

    model = Small_LLM_Model()
    full_prompt = f'''user_prompt: {prompts_list[0]}
    answer : "
    '''
    functions_text =  model.decode(list_functions)
    functions_text.append('"')
    prompt_ids = model.encode(full_prompt).squeeze().tolist()
    result = []
    for _ in range(30):
        logits = model.get_logits_from_input_ids(prompt_ids + result)
        masked = np.full_like(logits, -np.inf)

        for v in list_functions:
            for k in v:
                print(v)
                masked[v][k] = logits[v][k]
        cor = np.argmax(masked)
        result.append(cor)
        result_txt = mode.decode(result)
        if result_txt in functions_text:
            return result_txt


# def convert_to_token_ids(prompt_list : list) -> None:
#     full_prompt = prompt_list[0]
#     model = Small_LLM_Model()
#     return (model.encode(full_prompt).squeeze().tolist())

# def get_score(token_ids) -> None:
#     print("hi")
#     model = Small_LLM_Model()
#     print (model.get_logits_from_input_ids(token_ids))

