from llm_sdk.llm_sdk import Small_LLM_Model


def convert_to_token_ids(full_prompt: str) -> None:

    model = Small_LLM_Model()
    print(model.encode(full_prompt))

def llm_prompt(prompts: list, functions: list) -> None:
    
    for prompt in  prompts:
        prompt_text = prompt.prompt

        full_prompt = f"user: {prompt_text}"
        for function in functions:
            full_prompt +=f"\nfunction: name:{function.name} description: {function.description} parameters: "
            for param_name, param in function.parameters.items():
                full_prompt += f"{param_name} = {param.type} "
                # print(f"- {param_name}: {param.type}")
        convert_to_token_ids(full_prompt)
        break        

    #print(full_prompt)
