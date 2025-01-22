import json
import typing
if typing.TYPE_CHECKING:
    from _typeshed import SupportsWrite, SupportsRead


def change_lang() -> None:
    with open("local_data/config.json", "r", encoding="utf-8") as file: # type: SupportsRead[str | bytes]
        config: dict = json.load(file)
    old_lang = config["language"]
    new_lang = 'en' if old_lang == 'ru' else 'ru'
    config["language"] = new_lang
    with open("local_data/config.json", "w", encoding="utf-8") as file: # type: SupportsWrite[str]
        json.dump(config, file, indent=4, ensure_ascii=False)

change_lang()
