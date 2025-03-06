import tomllib
from _typeshed import SupportsRead


def get_script_tag() -> str:
    with open("pyproject.toml", "r", encoding="utf-8") as file: # type: SupportsRead
        script_release_tag: str = tomllib.load(file)['project']['version']

    return script_release_tag
