import  argparse
import parser
import start

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

    start.llm_prompt(prompts, functions)