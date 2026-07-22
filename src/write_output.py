from argparse import Namespace
from pathlib import Path


def write_output(args: Namespace, output_text: list) -> None:
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            for item in output_text:
                f.write(item)

    except Exception as error:
        print(f"Error writing output: {error}")
