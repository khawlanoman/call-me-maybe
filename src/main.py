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
    
    
    # all_prompt =[]
    # for p in prompts:
    #     generate_fn = start.convet(p, functions_name, functions, model,not_found_function)
    #     result = (state_machine.state_machine(state_machine.State, generate_fn, p, vocab, model))
    #     t_decode = model.decode(result)
    #     all_prompt.append(t_decode)

    
    # write_output.write_output(args, all_prompt)
        #print(t_decode)

    # all_prompts = (state_machine.generate_array(model, vocab, functions_name, functions, start, new_prompts, not_found_function))

    # write_output.write_output(args, all_prompts)

    
    
    function = start.convet(prompts[0], functions_name, functions, model,not_found_function)
    for i in functions:
        if i.name == function:
            t_func = i
    parameters = valid_prompt.parameter_of_function(t_func)
    result = ""

    for par in parameters:
        t_res = result + par
        value = found_parameters.found_a_number(
            model,
            np,
            prompts[0],
            function,
            t_res
        )

        result += f"{par}={value},"

    print(result)
    
