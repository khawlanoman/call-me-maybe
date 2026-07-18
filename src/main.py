import  argparse
import numpy as np
from . import parser
from . import start
from .  import state_machine
from . import read_vocab
from . import write_output
from . import valid_prompt
from . import found_parameters
from llm_sdk.llm_sdk import Small_LLM_Model

def parser_args() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--functions_definition", default="data/input/functions_definition.json")
    parser.add_argument("--input", default="data/input/function_calling_tests.json")
    parser.add_argument("--output", default="data/output/function_calls.json")
    args = parser.parse_args()
    return args
    #print(f"args= {args.input}")

if __name__ == "__main__":
    model = Small_LLM_Model()
    args = parser_args()
    prompts = parser.read_input_calling(args)

    new_prompts = valid_prompt.valid_prompt(prompts)
    #print(new_prompt)
    vocab = read_vocab.read_vocab(model)
    functions = parser.read_input_definition(args)
    # print(functions)
    not_found_function  ={ 
        "name":"fn_not_found", 
        "description":" this  function is for the",
        "parameters": {}
        }
    # list_prompt = start.llm_prompt(prompts)
    functions_name = start.function_token_ids(functions, model, not_found_function)
    #print(functions_name)
    # #print(functions_name)
    # result = []
    # for p in prompts:
        
    #     print(state_machine.state_machine( state_machine.State, "fn_add_number", p, vocab))


        # result.append(read_vocab.take_token_vocab(vocab, token))
        # print(result)
        #print(start.convet(p, functions_name, functions, model))

    # token_ids = start.convert_to_token_ids(list_prompt)
    #start.get_score(token_ids)
    
    
    all_prompt =[]
    all_params = []
    for index, p in enumerate(prompts):
        generate_fn = start.convet(p, functions_name, functions, model,not_found_function)
        for i in functions:
            if i.name == generate_fn:
                t_func = i
   
        parameters = valid_prompt.parameter_of_function(t_func)
        result_text = ""
        for k in parameters:
            t_res = result_text + k
            param_type = valid_prompt.check_parameter(t_func)
            if param_type == "number":
                rest = found_parameters.found_a_number(model,np,p,t_func,t_res)
            elif param_type == "string":
                rest = found_parameters.found_a_string_param(model,np, t_func.name,p,t_res)
            result_text += f"{k} ={rest},"
        params= {}
        for i in result_text.strip(',').split(','):
            key, value = i.split('=',1)
            params[key.strip()] = value.strip()

        all_params.append(params)
        result = (state_machine.state_machine(state_machine.State, generate_fn, p, vocab, model, all_params[index]))
        t_decode = model.decode(result)
        all_prompt.append(t_decode)
    #print(all_prompt)

    
    # write_output.write_output(args, all_prompt)
    #     print(t_decode)

    all_prompts = (state_machine.generate_array(model, vocab, functions_name, functions, start, new_prompts, not_found_function,all_params))

    write_output.write_output(args, all_prompts)

    
    """hna strnig"""
    # function = start.convet(prompts[0], functions_name, functions, model,not_found_function)
    # for i in functions:
    #     if i.name == generate_fn:
    #         t_func = i
   
    # parameters = valid_prompt.parameter_of_function(t_func)
    # result = ""
    # for k in parameters:
    #     t_res = result + k
    #     param_type = valid_prompt.check_parameter(t_func)
    #     if param_type == "number":
    #         rest = found_parameters.found_a_number(model,np,prompts[0],t_func,t_res)
    #     elif param_type == "string":
    #         rest = found_parameters.found_a_string_param(model,np, t_func.name,prompts[0],t_res)
    #     result += f"{k} ={rest},"

    # print(result)


    f"""hna numbers """
    # for par in parameters:
    #     t_res = result + par
    #     value = found_parameters.found_a_number(
    #         model,
    #         np,
    #         prompts[0],
    #         function,
    #         t_res
    #     )

    #     result += f"{par}={value},"

    # print(result)
    