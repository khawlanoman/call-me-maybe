import  argparse
from . import parser
from . import start
from .  import state_machine
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
    functions = parser.read_input_definition(args)

    list_prompt = start.llm_prompt(prompts)
    functions_name = start.function_token_ids(functions, model)
    #print(functions_name)
    for p in prompts:
        print(p)
        state_machine.state_machine( state_machine.State, "fn_add_number", p)
        print(start.convet(p, functions_name, functions, model))
    # token_ids = start.convert_to_token_ids(list_prompt)
    # start.get_score(token_ids)