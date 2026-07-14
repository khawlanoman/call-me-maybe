import json
def read_vocab(model) -> None:
    path = model.get_path_to_vocab_file()

    try:
        with open(path, "r") as file:
            lines =json.load(file)
            
    except FileNotFoundError as e:
        return (e)
    
    
    return lines

def take_token_vocab(vocab, token) -> None:
        
        result = vocab[token]
        return result