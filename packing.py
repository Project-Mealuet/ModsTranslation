from json import dump
import os
import zipfile


with open('pack.mcmeta', 'w', encoding='UTF-8') as pack_meta_file:
    dump({
        'pack': {
            'pack_format': 15, 
            'description': '零碎的Mod翻译整理\n作者/整理：Zack Zhu'
        }
    }, pack_meta_file, ensure_ascii=False, indent=4)

def zip_dir(path, ziph, ignore_file):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file != ignore_file:
                relative_path = os.path.relpath(os.path.join(root, file), os.path.join(path, '..'))
                ziph.write(os.path.join(root, file), relative_path)

zip_file_name = 'Minecraft-Mods-Translation-Zack.zip'
current_script = os.path.basename(__file__)
current_dir = '.'
with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zip_dir(current_dir, zipf, current_script)
