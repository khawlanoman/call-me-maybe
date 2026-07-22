
def valid_prompt(prompts) -> None:
    new_prompts = []
    for prompt in prompts:
        
        if '"' in prompt.prompt:
            new_prompt = prompt.prompt.replace('"','\\"')
            new_prompts.append(new_prompt)
        elif "\\" in prompt.prompt:
            new_prompt = prompt.prompt.replace('\\','\\\\')
            new_prompts.append(new_prompt)
        else:
            new_prompts.append(prompt.prompt)
           
    return new_prompts


def parameter_of_function(function) -> None:
    parameter = []
    for k,v in function.parameters.items():
        parameter.append(k)
    
    return parameter


def check_parameter(function) -> None:
    for k,v in function.parameters.items():
        return(v.type)
    return None

# def parameter_type(type_param) -> None:
#     if type_param == "number":
#         return ("found_a_number")
#     else if type_param == "string"
#         return 
    
#     else:
#         return 