from pathlib import Path

def write_output(args, output_text) -> None:
    # Output path from the command line
    output_path = Path(args.output)

    # Create parent directories if they don't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            for item in output_text:
                f.write(item)

    except Exception as error:
        print(f"Error writing output: {error}")