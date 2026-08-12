import shutil
from pathlib import Path

extensions: dict[str,list[str]] = {"Images": [".jpg", ".gif", ".png"], "Documents": [".pdf"]}

def set_up_directory(directory: Path, extensions: dict[str,list[str]]) -> None:

    folders_to_ensure = list(extensions.keys())

    folders_to_ensure.append("Other")

    for folder in folders_to_ensure:

        target_path = directory / folder

        target_path.mkdir(parents=True, exist_ok=True)
def get_category_for_extension(extension: str, extensions: dict[str,list[str]]) -> str:

    for key, value in extensions.items():
        if extension in value:
            return(key)
    return("Other")
def move_file(directory:Path, destination_directory:Path) -> None:

    _ = shutil.move(directory, destination_directory)

def organize_directory(directory:Path) -> None:
    for item in directory.iterdir():
        if item.is_file():
            extension = item.suffix
            source = directory / item.name
            destination = directory / get_category_for_extension(extension, extensions) / item.name
            move_file(source, destination)
            print("Item moved succesfully!")
if __name__ == "__main__":
    print("This is a file sorting script")
    home_dir = Path.home()
    downloads = home_dir / "Downloads"

    set_up_directory(downloads, extensions)

    organize_directory(downloads)





