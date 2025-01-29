import os
import shutil
from io import BytesIO
from zipfile import ZipFile
import requests
from local_data_func.get_script_release_tag import get_script_tag


class UpdateScript:

    GITHUB_REPO = "https://api.github.com/repos/koloideal/WordMath"

    @staticmethod
    def get_latest_release() -> dict:
        response = requests.get(f"{UpdateScript.GITHUB_REPO}/releases/latest")
        data = response.json()
        return {'tag': data['tag_name'],
                'url': data['zipball_url']}


    @staticmethod
    def download_new_release(zip_url):
        response = requests.get(zip_url)
        response.raise_for_status()

        with ZipFile(BytesIO(response.content)) as zip_file:
            zip_file.extractall("new_release")


    @staticmethod
    def upgrade_script():
        excluded_files = ['venv', '.venv', '.git', 'new_release']
        for obj in os.listdir():
            if obj not in excluded_files:
                if os.path.isfile(obj):
                    os.remove(obj)
                elif os.path.isdir(obj):
                    shutil.rmtree(obj)

        new_release = os.listdir('new_release')
        new_release_name = new_release[0] if new_release[0].startswith('koloideal-WordMath') else None
        path = f'new_release/{new_release_name}'
        all_files = os.listdir(path)
        for file in all_files:
            shutil.move(path + '/' + file, './' + file)

        shutil.rmtree('new_release')


    @staticmethod
    def start_update() -> bool:
        existing_release_tag: str = get_script_tag()
        latest_release: dict = UpdateScript.get_latest_release()
        latest_release_tag = latest_release['tag']
        latest_release_url = latest_release['url']

        if latest_release_tag != existing_release_tag:
            UpdateScript.download_new_release(latest_release_url)
            UpdateScript.upgrade_script()
            return True
        else:
            return False


