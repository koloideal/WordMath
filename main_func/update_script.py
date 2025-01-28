import os
from io import BytesIO
from zipfile import ZipFile
import requests
from local_data_func.get_script_release_tag import get_script_tag


GITHUB_REPO = "https://api.github.com/repos/koloideal/WordMath"


def get_latest_release() -> dict | bool:
    try:
        response = requests.get(f"{GITHUB_REPO}/releases/latest")
        data = response.json()
        return {'tag': data['tag_name'],
                'url': data['zipball_url']}
    except requests.RequestException:
        return False


def update_script(zip_url):
    try:
        response = requests.get(zip_url)
        response.raise_for_status()

        with ZipFile(BytesIO(response.content)) as zip_file:
            zip_file.extractall("update_temp")

        for root, dirs, files in os.walk("update_temp"):
            for file in files:
                if file.endswith(".py"):
                    source_path = os.path.join(root, file)
                    destination_path = os.path.join(os.getcwd(), file)
                    print(source_path)
                    print(destination_path)
                    # os.replace(source_path, destination_path)
        '''
        for root, dirs, files in os.walk("update_temp", topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir("update_temp")'''

        print("Скрипт успешно обновлен!")
    except Exception as e:
        print(f"Ошибка при обновлении: {e}")


