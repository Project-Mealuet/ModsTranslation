import json


with open('zh_cn.json', 'r', encoding='UTF-8') as origin_file:
    origin_content = json.load(origin_file)
with open('new.json', 'r', encoding='UTF-8') as new_file:
    new_content = json.load(new_file)
for key in origin_content:
    if key in new_content:
        origin_content[key] = new_content[key]
with open('zh_cn_new.json', 'w', encoding='UTF-8') as dist_file:
    json.dump(origin_content, dist_file, indent=4, ensure_ascii=False)