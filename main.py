from pathlib import Path
import shutil

extensions = {"Images": [".jpg", ".gif", "png"], "Documents": [".pdf"]}

def set_up_directory(directory: Path, extensions: dict) -> None:

    folders_to_ensure = list(extensions.keys())

    for folder in folders_to_ensure:

        target_path = directory / folder

        target_path.mkdir(parents=True, exist_ok=True)
def get_category_for_extension(extension: str, categories: dict) -> str:

    for value in categories:
        if extension in categories[value]:
            return(value)
def move_file(directory:Path, destination_directory:Path) -> None:

    shutil.move(directory, destination_directory)


