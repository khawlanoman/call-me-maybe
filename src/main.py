import  argparse


def parser_args() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--functions_definition", default="data/input/functions_definition.json")
    parser.add_argument("--input", default="data/input/function_calling_tests.json")
    parser.add_argument("--output", default="data/output/function_calls.json")
    args = parser.parse_args()
    #print(f"args= {args}")

if __name__ == "__main__":
    parser_args()