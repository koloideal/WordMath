import tomllib


def get_script_tag() -> str:
    with open("pyproject.toml", "rb", encoding="utf-8") as file:
        script_release_tag: str = tomllib.load(file)['project']['version']

    return script_release_tag
