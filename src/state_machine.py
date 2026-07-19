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
    PARAMS_key = 9
    PARAMS_COLON = 10
    PARAMS_VALUE = 11
    PARAMS_COMMA = 12
    PARAMS_CLOSE = 13
    CLOSE_BRACE = 14
    END = 15

def  state_machine( State, function_n, prompt, vocab, model, params) -> None:
    state = State.START
    result = []
    #for i in range(8):
    new_line = model.encode("\n").squeeze().tolist()
    tab = model.encode("\t").squeeze().tolist()
    if state == State.START:
        tab_new_line = model.encode("\n\t").squeeze().tolist()
        for i in tab_new_line:
            result.append(i)
        result.append(read_vocab.take_token_vocab(vocab, "{"))
        result.append(new_line)
        result.append(tab)
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
        token_ids = model.encode(f'"{prompt}"').squeeze().tolist()
        for i in token_ids:
            result.append(i)
        state = State.PROMPT_VALUE
    
    if state == State.PROMPT_VALUE:
        result.append(read_vocab.take_token_vocab(vocab,","))
        result.append(new_line)
        result.append(tab)
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
        state = State.PARAMS_key
    # #\
    if state == State.PARAMS_key:
        result.append(read_vocab.take_token_vocab(vocab,","))
        result.append(new_line)
        state = State.PARAMS_COLON

    if state == State.PARAMS_COLON:
        result.append(tab)
        result.append(tab)
        token_ids =  model.encode('"parameters"').squeeze().tolist()
        for i in token_ids:
            result.append(i)
        state = State.PARAMS_VALUE

    if state == State.PARAMS_VALUE:
        result.append(read_vocab.take_token_vocab(vocab,":"))
        result.append(read_vocab.take_token_vocab(vocab,"{"))
        state = State.PARAMS_COMMA
    
    if state == State.PARAMS_COMMA:
        param = params.items()
        for index, (k, v)  in enumerate(param):
            #result.append(read_vocab.take_token_vocab(vocab, k))
            token_ids =  model.encode(f'"{k}"').squeeze().tolist()
            for i in token_ids:
                result.append(i)
            result.append(read_vocab.take_token_vocab(vocab,":"))
            if isinstance(v, str):
                try:
                    float(v)
                    token_ids = model.encode(f' {v}').squeeze().tolist()
                except ValueError:
                    token_ids = model.encode(f' "{v}"').squeeze().tolist()
            else:
                token_ids = model.encode(f' {v}').squeeze().tolist()
            for i in token_ids:
                result.append(i)
            #result.append(read_vocab.take_token_vocab(vocab, v))
            if index != len(param) -1:
                result.append(read_vocab.take_token_vocab(vocab,","))
        result.append(read_vocab.take_token_vocab(vocab,"}"))
        state = State.PARAMS_CLOSE

    if state == State.PARAMS_CLOSE:
        result.append(new_line)
        result.append(tab)
        result.append(read_vocab.take_token_vocab(vocab,"}"))
        state = State.CLOSE_BRACE
    
    if state == State.CLOSE_BRACE:
        state = State.END
    
    if state == State.END:
        return result
    
    return result



def generate_array(model, vocab, outputs):

    result = []

    start_list = read_vocab.take_token_vocab(vocab, "[")
    end_list = read_vocab.take_token_vocab(vocab, "]")
    comma = read_vocab.take_token_vocab(vocab, ",")
    new_line = model.encode("\n").squeeze().tolist()

    result.append(model.decode(start_list))

    for i, output in enumerate(outputs):

        result.append(output)

        if i != len(outputs) - 1:
            result.append(model.decode(comma))

    result.append(model.decode(new_line))
    result.append(model.decode(end_list))

    return result