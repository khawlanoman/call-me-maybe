from llm_sdk.llm_sdk import Small_LLM_Model


def llm_prompt(prompts: list, functions: list) -> None:
    prompt_list = []
    for prompt in  prompts:
        prompt_text = prompt.prompt

        full_prompt = f"user: {prompt_text}"
        for function in functions:
            full_prompt +=f"\nfunction: name:{function.name} description: {function.description} parameters: "
            for param_name, param in function.parameters.items():
                full_prompt += f"{param_name} = {param.type} "
                # print(f"- {param_name}: {param.type}")
        prompt_list.append(full_prompt)

    return (prompt_list)


def convert_to_token_ids(prompt_list : list) -> None:
    full_prompt = prompt_list[0]
    model = Small_LLM_Model()
    return (model.encode(full_prompt))

def get_score(token_ids) -> None:
    print("hi")
    model = Small_LLM_Model()
    print (model.get_logits_from_input_ids(token_ids))

