import os
import shutil


def upgrade_script():
    new_release = os.listdir('new_release')
    new_release_name = new_release[0] if new_release[0].startswith('koloideal-WordMath') else None
    path = f'update_temp/{new_release_name}'
    all_files = os.listdir(path)
    for file in all_files:
        shutil.move(path+'/'+file, './'+file)
