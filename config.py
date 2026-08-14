import json
from pathlib import Path

config_file:Path = Path("config.json")

default_config: dict[str, list[str]] = {
        "Images" : [".jpg", ".gif", ".png"],
        "Documents" : [".pdf", ".docx", ".pages"],
        "Audio" : [".mp3", ".wav"],
        "Video" : [".mp4", ".mov"],
}