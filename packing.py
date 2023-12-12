from json import dump
import os
import zipfile
from datetime import datetime


current_date = datetime.now().strftime('%Y/%m/%d')

with open('pack.mcmeta', 'w', encoding='UTF-8') as pack_meta_file:
    dump({
        'pack': {
            'pack_format': 15, 
            'description': f'零碎的Mod翻译整理\n打包时间：{current_date}'
        }
    }, pack_meta_file, ensure_ascii=False, indent=4)

def zip_specific_items(zipf, items):
    for item in items:
        if os.path.isdir(item):
            for root, dirs, files in os.walk(item):
                for file in files:
                    zipf.write(os.path.join(root, file),
                               os.path.relpath(os.path.join(root, file),
                                           os.path.join(item, '..')))
        elif os.path.isfile(item):
            zipf.write(item)

zip_file_name = 'Minecraft-Mods-Translation-Zack.zip'
items_to_zip = ['assets', 'pack.png', 'pack.mcmeta']  # 指定要打包的目录和文件

with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zip_specific_items(zipf, items_to_zip)
