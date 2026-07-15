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
        result.append(new_line)
        state = State.FUNCTION_NAME
    
    if state == State.FUNCTION_NAME:
        result.append(tab)
        result.append(read_vocab.take_token_vocab(vocab,"}"))
        state = State.CLOSE_BRACE
    
    if state == State.CLOSE_BRACE:
        state = State.END
    
    if state == State.END:
        return result
    
    return result


def generate_array(model, vocab,functions_name, functions,start, prompts,not_found_function) -> None:
    all_prompt = []
    start_list = read_vocab.take_token_vocab(vocab, "[")
    end_list = read_vocab.take_token_vocab(vocab, "]")
    comma = read_vocab.take_token_vocab(vocab, ",")
    new_line = model.encode("\n").squeeze().tolist()

    all_prompt.append(model.decode(start_list))
   # all_prompt.append(model.decode(tab_new_line))
    print(prompts)
    for p in prompts:
        generate_fn = start.convet(p, functions_name, functions, model,not_found_function)
        result = (state_machine( State, generate_fn, p, vocab, model))
        t_decode = model.decode(result)
        all_prompt.append(t_decode)
        if  p != prompts[-1]:
            all_prompt.append(model.decode(comma))
    all_prompt.append(model.decode(new_line))
    all_prompt.append(model.decode(end_list))

    return all_prompt
