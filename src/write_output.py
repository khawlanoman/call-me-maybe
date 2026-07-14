
def write_output(args, output_text) -> None:

    #print(args.output)
    try:
        with open(args.output, "w+") as file :
            for i in output_text:
                file.write(i)
    
    except FileNotFoundError as error:
        return(error)
    
    