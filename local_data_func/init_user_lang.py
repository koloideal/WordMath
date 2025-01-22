import json
import os


def init_user_lang(pc_name) -> None:
    is_users_config_exists: bool = os.path.exists('local_data/config.json')
    os.makedirs('local_data', exist_ok=True)
    if not is_users_config_exists:
        config: dict = {'pc_name': pc_name,
                        'language': 'en'}
        with open("local_data/config.json", "w", encoding="utf-8") as file:
            json.dump(config, file, indent=4)

