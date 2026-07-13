import  argparse
from . import parser
from . import start

def parser_args() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--functions_definition", default="data/input/functions_definition.json")
    parser.add_argument("--input", default="data/input/function_calling_tests.json")
    parser.add_argument("--output", default="data/output/function_calls.json")
    args = parser.parse_args()
    return args
    #print(f"args= {args.input}")

if __name__ == "__main__":
    args = parser_args()
    prompts = parser.read_input_calling(args)
    functions = parser.read_input_definition(args)

    list_prompt = start.llm_prompt(prompts)
    print(functions_name = start.function_token_ids(functions))

   # print(start.convet(list_prompt, functions_name))
    # token_ids = start.convert_to_token_ids(list_prompt)
    # start.get_score(token_ids)