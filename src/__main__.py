import argparse
import sys
import numpy as np
from . import models
from . import parser
from . import start
from typing import Any
from . import state_machine
from . import read_vocab
from . import write_output
from . import valid_prompt
from . import found_parameters
from llm_sdk.llm_sdk import Small_LLM_Model


def parser_args() -> Any:
    parser = argparse.ArgumentParser()
    parser.add_argument("--functions_definition",
                        default="data/input/functions_definition.json")
    parser.add_argument("--input",
                        default="data/input/function_calling_tests.json")
    parser.add_argument("--output",
                        default="data/output/function_calls.json")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    try:
        model = Small_LLM_Model()
        args = parser_args()
        prompts = parser.read_input_calling(args)

        new_prompts = valid_prompt.valid_prompt(prompts)

        vocab = read_vocab.read_vocab(model)
        functions = parser.read_input_definition(args)

        not_found_function = models.Function_definition(
            name="fn_unknown",
            description="Handle user requests that do not match any available function.", # noqa
            parameters={},
            returns=models.Returns(type="void")
        )

        functions_name = start.function_token_ids(functions, model,
                                                  not_found_function)

        all_prompt = []
        all_params = []
        for index, p in enumerate(new_prompts):

            generate_fn = start.convet(p, functions_name, functions,
                                       model, not_found_function)
            t_func = None
            for i in functions:
                if i.name == generate_fn:
                    t_func = i
                    break
            if t_func is None:
                t_func = not_found_function
            params = {}
            param_type = ""
            print(t_func)
            if len(t_func.parameters) > 0:
                parameters = valid_prompt.parameter_of_function(t_func)
                
                result_text = ""
                for k in parameters:

                    t_res = result_text + k
                    
                    param_type = valid_prompt.check_parameter(t_func)
                    
                    if param_type == "string":

                        rest = found_parameters.found_a_string_param(model,
                                                                    np, t_func.name,p,t_res, k) # noqa
                        result_text += f'{k}="{rest}", '
                    else:

                        rest = found_parameters.found_a_number(model, np,
                                                               p, t_func.name,
                                                               t_res)
                        result_text += f'{k}={rest},\n'

                    params[k] = rest.strip("\n")
                    print(params[k], rest)
            all_params.append(params)
            if generate_fn is None or param_type is None:
                raise ValueError("error")
            result = (state_machine.state_machine(state_machine.State,
                                                  generate_fn, p, vocab,
                                                  model,
                                                  all_params[index],
                                                  param_type))

            t_decode = model.decode(result)
            all_prompt.append(t_decode)

        all_prompts = (state_machine.generate_array(model, vocab, all_prompt))

        write_output.write_output(args, all_prompts)

    except KeyboardInterrupt:
        sys.exit(0)
