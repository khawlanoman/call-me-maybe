
def valid_prompt(prompts) -> None:
    new_prompts = []
    for prompt in prompts:
        
        if '"' in prompt.prompt:
            new_prompt = prompt.prompt.replace('"','\\"')
            new_prompts.append(new_prompt)
            
        else:
            new_prompts.append(prompt.prompt)
           
    return new_prompts