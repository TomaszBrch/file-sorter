import json
from pathlib import Path

config_file:Path = Path("config.json")

default_config: dict[str, list[str]] = {
        "Images" : [".jpg", ".gif", ".png"],
        "Documents" : [".pdf", ".docx", ".pages"],
        "Audio" : [".mp3", ".wav"],
        "Video" : [".mp4", ".mov"],
        "Installers" : [".exe", ".dmg"],
        "Archives" : [".rar", ".zip"]
}
def load_or_create_config(config_path : Path) -> dict[str,list[str]]:
    if not config_path.exists():
        print(f"No config file found. Creating default config at {config_path}...")

        with config_path.open("w") as file:
            json.dump(obj=default_config, fp=file, indent=4)
        return default_config
    with config_path.open("r") as file:
        data = json.load(fp=file)  # pyright: ignore[reportAny]

        if isinstance(data, dict):
            return data  # pyright: ignore[reportUnknownVariableType]
        else:
            print("Warning: config.json is improperly formatted. Using defaults")
            return default_config


