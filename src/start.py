
def llm_prompt(prompts: list, functions: list) -> None:
    
    for prompt in  prompts:
        prompt_text = prompt.prompt

        full_prompt = f"user: {prompt_text}"
        for function in functions:
            full_prompt +=f"\nfunction: name:{function.name} description: {function.description} parameters: "
            for param_name, param in function.parameters.items():
                full_prompt += f"{param_name} = {param.type} "
                # print(f"- {param_name}: {param.type}")
        break        

    print(full_prompt)

