
def write_output(args, output_text) -> None:

    #print(args.output)
    try:
        with open(args.output, "w+") as file :
            print(args.output)
            file.write(output_text)
    
    except FileNotFoundError as error:
        return(error)
    
    