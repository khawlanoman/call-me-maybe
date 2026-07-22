from pydantic import ValidationError
import json
from . import models
import sys
from argparse import Namespace


def read_input_calling(files: Namespace) -> list:
    try:
        input_file = files.input

        with open(input_file, 'r') as file:
            try:
                lines = json.load(file)
            except json.JSONDecodeError as e:
                print(f"{e}")
                sys.exit(0)

    except FileNotFoundError:
        print("error : file not found")
        sys.exit(0)

    prompts_list = []
    for line in lines:
        try:
            lin = models.Function_calling_test.model_validate(line)
            prompts_list.append(lin)
        except ValidationError as e:
            print(f"invalid prompt:{e}")
            sys.exit(0)

    return (prompts_list)


def read_input_definition(files: Namespace) -> list:
    try:
        input_definition = files.functions_definition

        with open(input_definition, 'r') as file:
            try:
                lines = json.load(file)
            except json.JSONDecodeError as e:
                print(f"error:{e}")
                sys.exit(0)

    except FileNotFoundError:
        print("error : file not found")
        sys.exit(0)
    function_list = []
    for line in lines:
        try:
            l_check = models.Function_definition.model_validate(line)
            function_list.append(l_check)
        except ValidationError as e:
            print(f"invalid function:{e}")
            sys.exit(0)

    return (function_list)
