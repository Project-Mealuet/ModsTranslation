import os, json, shutil


def merge_dicts(dict1, dict2):
    merging_dict = dict1.copy()
    merging_dict.update(dict2)
    return merging_dict

for translated_file in os.listdir('_assets'):
    for i18n_file in os.listdir('assets'):
        if i18n_file == translated_file:
            break
    else:
        try:
            os.makedirs(f'assets/{translated_file}/lang', exist_ok=True)
            shutil.copy(f'_assets/{translated_file}/lang/zh_cn.json', f'assets/{translated_file}/lang/zh_cn.json')
        except FileNotFoundError:
            continue
    if os.path.exists(f'assets/{translated_file}/lang/zh_cn.json'):
        translated_file_content = open(f'_assets/{translated_file}/lang/zh_cn.json', encoding='UTF-8')
        i18n_file_content = open(f'assets/{translated_file}/lang/zh_cn.json', encoding='UTF-8')
        merged_dict = merge_dicts(json.load(translated_file_content), json.load(i18n_file_content))
        os.makedirs(f'assets/{translated_file}/lang', exist_ok=True)
        with open(f'assets/{translated_file}/lang/zh_cn.json', 'w', encoding='UTF-8') as file_translated:
            json.dump(merged_dict, file_translated, indent=4, ensure_ascii=False)
        translated_file_content.close()
        i18n_file_content.close()
    else:
        try:
            os.makedirs(f'assets/{translated_file}/lang', exist_ok=True)
            shutil.copy(f'_assets/{translated_file}/lang/zh_cn.json', f'assets/{translated_file}/lang/zh_cn.json')
        except FileNotFoundError:
            continue

shutil.rmtree('_assets')
os.makedirs('_assets', exist_ok=True)