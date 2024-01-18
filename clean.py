import os
import json
import shutil

def is_empty_json(file_path):
    """ Check if a JSON file is empty or not. """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return not bool(data)  # Returns True if JSON is empty
    except json.JSONDecodeError:
        return True  # File is empty or not a valid JSON

def should_delete_folder(folder_path):
    """ Check if the folder should be deleted according to the criteria. """
    lang_folder = os.path.join(folder_path, 'lang')
    if not os.path.exists(lang_folder) or not os.listdir(lang_folder):
        return True
    zh_cn_path = os.path.join(lang_folder, 'zh_cn.json')
    if os.path.exists(zh_cn_path) and is_empty_json(zh_cn_path):
        return True
    return False

def delete_folders(root_folder):
    """ Delete folders based on the specified criteria. """
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        if os.path.isdir(folder_path) and should_delete_folder(folder_path):
            print(f"Deleting folder: {folder_path}")
            shutil.rmtree(folder_path)  # Use os.removedirs to delete non-empty directories

path_to_assets = 'assets'
delete_folders(path_to_assets)
