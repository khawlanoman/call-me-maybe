from enum import Enum
from . import read_vocab
class State(Enum):
    START = 0
    OPEN_BRACE = 1
    PROMPT_KEY = 2
    PROMPT_COLON= 3
    PROMPT_VALUE = 4
    COMMA = 5
    NAME_KEY = 6
    NAME_COLON = 7
    FUNCTION_NAME = 8
    CLOSE_BRACE = 9
    END = 10

def  state_machine( State, function_n, prompt, vocab, model) -> None:
    state = State.START
    result = []
    #for i in range(8):
    new_line = model.encode("\n").squeeze().tolist()
    tab = model.encode("\t").squeeze().tolist()
    if state == State.START:
        result.append(read_vocab.take_token_vocab(vocab, "{"))
        result.append(new_line)
        result.append(tab)
        state = State.OPEN_BRACE

    if state == State.OPEN_BRACE:

        token_ids = model.encode('"prompt"').squeeze().tolist()
        for i in token_ids:
            result.append(i)
        state = State.PROMPT_KEY

    if state == State.PROMPT_KEY:
        result.append(read_vocab.take_token_vocab(vocab, ":"))
        state = State.PROMPT_COLON
    
    if state == State.PROMPT_COLON:
        token_ids = model.encode(f'"{prompt.prompt}"').squeeze().tolist()
        for i in token_ids:
            result.append(i)
        state = State.PROMPT_VALUE
    
    if state == State.PROMPT_VALUE:
        result.append(read_vocab.take_token_vocab(vocab,","))
        result.append(new_line)
        result.append(tab)
        state = State.COMMA
    
    if state == State.COMMA:
        token_ids = model.encode('"name"').squeeze().tolist()
        for i in token_ids:
            result.append(i)
        state = State.NAME_KEY
    
    if state == State.NAME_KEY:
        result.append(read_vocab.take_token_vocab(vocab, ":"))
        state = State.NAME_COLON

    if state == State.NAME_COLON:
        token_ids = model.encode(f'"{function_n}"').squeeze().tolist()
        for i in token_ids:
            result.append(i)
        result.append(new_line)
        state = State.FUNCTION_NAME
    
    if state == State.FUNCTION_NAME:
        result.append(read_vocab.take_token_vocab(vocab,"}"))
        state = State.CLOSE_BRACE
    
    if state == State.CLOSE_BRACE:
        state = State.END
    
    if state == State.END:
        return result
    
    return result

        # if state == State.START:
        #     print("{")
        #     token = "{"
        #     state = State.OPEN_BRACE

        # if state == State.OPEN_BRACE:
        #     print('"prompt"')
        #     token = '"prompt"'
        #     state = State.PROMPT
        
        # if state == State.PROMPT:
        #     print(":")
        #     token = ":"
        #     state = State.COLON
        
        # if state == State.COLON:
        #     print(f'"{prompt}"')
        #     token = ":"
        #     state = State.PROMPT_CONT

        # if state == State.PROMPT_CONT:
        #     print(",")
        #     #token = 
        #     state = State.COMMA

        # if state == State.COMMA:
        #     print('"name"')
        #     token = '"name"'
        #     state = State.NAME_COLON
        
        # if state == State.NAME_COLON:
        #     print("")

        # if state == State.NAME_KEY:
        #     print(f'"{function_n}"')
        #     #token = ","
        #     state = State.COLON
        
        # if state == State.FUNCTION_NAME:
        #     print("}")
        #     token = "}"
        #     state = State.CLOSE_BRACE
        
        # if state == State.CLOSE_BRACE:
        #     state = State.END
        
        # if state == State.END:
        #    break