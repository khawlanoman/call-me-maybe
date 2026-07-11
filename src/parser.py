import json

def parsing(files) -> None:
    prompts_list = []
    try:
        print("HI")
        input_file = files.input
        
        with open(input_file,'r') as file:
            lines = json.load(file)

    except FileNotFoundError as e:
       print("error")
    
    for line in lines:
        prompts_list.append(line)

    print(prompts_list)