from . import models

def valid_prompt(prompts: list) -> list:
    new_prompts = []
    for prompt in prompts:

        if '"' in prompt.prompt:
            new_prompt = prompt.prompt.replace('"', '\\"')
            new_prompts.append(new_prompt)
        elif "\\" in prompt.prompt:
            new_prompt = prompt.prompt.replace('\\', '\\\\')
            new_prompts.append(new_prompt)
        else:
            new_prompts.append(prompt.prompt)

    return new_prompts


def parameter_of_function(function: models.Function_definition) -> list:
    parameter = []
    for k, v in function.parameters.items():
        parameter.append(k)

    return parameter


def check_parameter(function: models.Function_definition) -> str | None:
    for k, v in function.parameters.items():
        return (f"{v.type}")
    return None
