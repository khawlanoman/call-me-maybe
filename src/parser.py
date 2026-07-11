import json
import sys
def read_input_calling(files) -> None:
    
    try:
        print("HI")
        input_file = files.input
        
        with open(input_file,'r') as file:
            lines = json.load(file)

    except FileNotFoundError as e:
       print("error")
       sys.exit(0)
    prompts_list = []
    for line in lines:
        prompts_list.append(line)

    print(prompts_list)
    #return (prompts_list)

def read_input_definition(files) -> None:
    try:
        input_definition = files.functions_definition

        with open(input_definition, 'r') as file:
            lines = json.load(file)

    except FileNotFoundError as e:
        sys.exit(0)
    function_list = []
    for line in lines:
        function_list.append(line)
    
    print(function_list)


