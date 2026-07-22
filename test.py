from llm_sdk.llm_sdk import Small_LLM_Model
import numpy as np



def main() -> str:
    model = Small_LLM_Model()
    # user_req = "is rabat a country ?"

    # allowed = ["YES", "NO", '"']
    # allowed_tkn = []
    # for v in allowed:
    #     allowed_tkn.append(model.encode(v).squeeze().tolist())
    
    # prompt = f'''Answer on the user request wiht YES or NO
    # User Request : {user_req}
    # Answer: "
    # '''
    # prompt_ids = model.encode(prompt).squeeze().tolist()
    # resulr = []
    # for _ in range(30):
    #         logits = model.get_logits_from_input_ids(prompt_ids + resulr)
    #         masked = np.full_like(logits, -np.inf)

    #         for tid in allowed_tkn:
    #             masked[tid] = logits[tid]
    #         correct = np.argmax(masked)
    #         resulr.append(correct)
    #         txt = model.decode(resulr)
    #         if txt in allowed:
    #             return txt

    path = model.get_path_to_vocab_file()

    return (path)
if __name__ == "__main__":

    print(main())






# ////////////////////////////////

# [
#   {
#     "prompt": "What is the sum of 2 and 3?"
#   },
#   {
#     "prompt": "What is the sum of 265 and 345?"
#   },
#   {
#     "prompt": "Greet shrek"
#   },
#   {
#     "prompt": "Greet john"
#   },
#   {
#     "prompt": "Reverse the string 'hello'"
#   },
#   {
#     "prompt": "Reverse the string 'world'"
#   },
#   {
#     "prompt": "What is the square root of 16?"
#   },
#   {
#     "prompt": "Calculate the square root of 144"
#   },
#   {
#     "prompt": "Replace all numbers in \"Hello 34 I'm 233 years old\" with NUMBERS"
#   },
#   {
#     "prompt": "Replace all vowels in 'Programming is fun' with asterisks"
#   },
#   {
#     "prompt": "Substitute the word 'cat' with 'dog' in 'The cat sat on the mat with another cat'"
#   }
# ]

# ////////////////////////
# [
#   {
#     "name": "fn_add_numbers",
#     "description": "Add two numbers together and return their sum.",
#     "parameters": {
#       "a": {
#         "type": "number"
#       },
#       "b": {
#         "type": "number"
#       }
#     },
#     "returns": {
#       "type": "number"
#     }
#   },
#   {
#     "name": "fn_greet",
#     "description": "Generate a greeting message for a person by name.",
#     "parameters": {
#       "name": {
#         "type": "string"
#       }
#     },
#     "returns": {
#       "type": "string"
#     }
#   },
#   {
#     "name": "fn_reverse_string",
#     "description": "Reverse a string and return the reversed result.",
#     "parameters": {
#       "s": {
#         "type": "string"
#       }
#     },
#     "returns": {
#       "type": "string"
#     }
#   },
#   {
#     "name": "fn_get_square_root",
#     "description": "Calculate the square root of a number.",
#     "parameters": {
#       "a": {
#         "type": "number"
#       }
#     },
#     "returns": {
#       "type": "number"
#     }
#   },
#   {
#     "name": "fn_substitute_string_with_regex",
#     "description": "Replace all occurrences matching a regex pattern in a string.",
#     "parameters": {
#       "source_string": {
#         "type": "string"
#       },
#       "regex": {
#         "type": "string"
#       },
#       "replacement": {
#         "type": "string"
#       }
#     },
#     "returns": {
#       "type": "string"
#     }
#   }
# ]


find /home/khnoman-type f -printf '%s %p\n' 2>/dev/null | sort -rn | head -20 | awk '{size=$1/1024/1024; printf "%.2f MB\t%s\n", size, $2}'
export PIP_CACHE_DIR=/home/khnoman/goinfre/pip-cache
export POETRY_CACHE_DIR=/home/khnoman/goinfre/pypoetry-cache
export PYTHONUSERBASE=/home/khnoman/goinfre/python-user
export UV_CACHE_DIR=/home/khnoman/goinfre/cash/
mkdir -p /home/khnoman/goinfre/venv
export UV_PROJECT_ENVIRONMENT=/home/khnoman/goinfre/venv/
export XDG_CACHE_HOME=/home/khnoman/goinfre/
export XDG_DATA_HOME=/home/khnoman/goinfre/