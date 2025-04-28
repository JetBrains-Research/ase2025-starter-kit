import os
import jsonlines
import random
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument("--stage", type=str, default="start", help="Stage of the project")
argparser.add_argument("--strategy", type=str, default="random", help="Stage of the project")
args = argparser.parse_args()

stage = args.stage
strategy = args.strategy

print(f"Running the {strategy} baseline for stage '{stage}'")

# token used to separate different files in the context
FILE_SEP_SYMBOL = "<|file_sep|>"
# format to compose context from a file
FILE_COMPOSE_FORMAT = "{file_sep}{file_name}\n{file_content}"



def find_random_python_file(root_dir: str, min_lines: int = 10) -> str:
    """
    Select a random Python file in the given directory and its subdirectories.
    :param root_dir: Directory to search for Python files.
    :param min_lines: Minimum number of lines required in the file.
    :return: Selected random file.
    """
    python_files = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".py"):
                file_path = os.path.join(dirpath, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        if len(lines) >= min_lines:
                            python_files.append(file_path)
                except Exception as e:
                    # Optional: handle unreadable files
                    # print(f"Could not read {file_path}: {e}")
                    pass

    return random.choice(python_files) if python_files else None

# Path to the file with completion points
completion_points_file = os.path.join("data", f"completion_points_{stage}.jsonl")

# Path to the file to store predictions
predictions_file = os.path.join("predictions", f"{stage}_single_{strategy}.jsonl")

with jsonlines.open(completion_points_file, 'r') as reader:
    with jsonlines.open(predictions_file, 'w') as writer:
        for datapoint in reader:
            # Identify the repository storage for the datapoint
            repo_path = datapoint['repo'].replace("/", "__")
            repo_revision = datapoint['revision']
            root_directory = os.path.join("data", f"repositories_{stage}", f"{repo_path}-{repo_revision}")

            # Run the baseline strategy
            if strategy == "random":
                file_name = find_random_python_file(root_directory)
            elif strategy == "bm25":
                ...
            else:
                raise ValueError(f"Unknown strategy: {strategy}")

            # Compose the context from the selected file
            file_content = open(file_name, 'r', encoding='utf-8').read()
            clean_file_name = file_name[len(root_directory) + 1:]
            context = FILE_COMPOSE_FORMAT.format(file_sep=FILE_SEP_SYMBOL, file_name=clean_file_name, file_content=file_content)

            # Write the result to the prediction file
            print(f"Picked file: {clean_file_name}")
            writer.write({"context": context})
