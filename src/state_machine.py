from enum import Enum

class State(Enum):
    START = 0
    OPEN_BRACE = 1
    PROMPT = 2
    PROMPT_CONT = 3
    NAME_KEY = 4
    COLON = 5
    COMMA = 8
    FUNCTION_NAME = 6
    CLOSE_BRACE = 7
    END = 9

def  state_machine( State, function_n, prompt) -> None:
    state = State.START
    
    for i in range(8):
        if state == State.START:
            print("{")
            token = "{"
            state = State.OPEN_BRACE

        if state == State.OPEN_BRACE:
            print('"prompt"')
            token = '"prompt"'
            state = State.PROMPT
        
        if state == State.PROMPT:
            print(":")
            token = ":"
            state = State.COLON
        
        if state == State.COLON:
            print(f'"{prompt}"')
            token = ":"
            state = State.PROMPT_CONT

        if state == State.PROMPT_CONT:
            print(",")
            #token = 
            state = State.COMMA
        
        if state == State.COMMA:
            print('"name"')
            token = '"name"'
            state = State.NAME_KEY

        if state == State.NAME_KEY:
            print(f'"{function_n}"')
            #token = ","
            state = State.FUNCTION_NAME
        
        if state == State.FUNCTION_NAME:
            print("}")
            token = "}"
            state = State.CLOSE_BRACE
        
        if state == State.CLOSE_BRACE:
            state = State.END
        
        if state == State.END:
           break