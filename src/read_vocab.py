import json
from typing import Any
import sys


def read_vocab(model: Any) -> Any:
    path = model.get_path_to_vocab_file()

    try:
        with open(path, "r") as file:
            lines = json.load(file)

    except FileNotFoundError as e:
        print(f"error: {e}")
        sys.exit(0)

    return (lines)


def take_token_vocab(vocab: dict[str, Any], token: str) -> Any:

    result = vocab[token]
    return (result)
