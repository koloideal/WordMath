import tomllib


def get_script_tag() -> str:
    with open("pyproject.toml", "rb") as file:
        script_release_tag: str = tomllib.load(file)['project']['version']

    return script_release_tag
