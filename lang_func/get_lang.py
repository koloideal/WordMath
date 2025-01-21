import json


def get_lang() -> str:
    with open("local_data/config.json", "r", encoding="utf-8") as file:
        config: dict = json.load(file)
    language: str = config["language"]

    return language
