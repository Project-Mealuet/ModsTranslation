import os
import json
import csv

def merge_json_files(root_dir):
    merged_data = {}

    for root, dirs, files in os.walk(root_dir):
        if 'lang' in dirs:
            lang_dir = os.path.join(root, 'lang')
            json_file_path = os.path.join(lang_dir, 'zh_cn.json')
            if os.path.exists(json_file_path):
                with open(json_file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    merged_data.update(data)  # Update the main dictionary with new entries

    return merged_data

def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def json_to_csv(json_data, csv_file_path):
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['key', 'value'])  # header
        for key, value in json_data.items():
            csvwriter.writerow([key, value])

# Define the root directory and file paths
root_directory = 'assets'
output_json_file = os.path.join('dict', 'zh_cn_mods.json')
output_csv_file = os.path.join('dict', 'zh_cn_mods.csv')

# Merge the JSON files
merged_json = merge_json_files(root_directory)

# Save the merged JSON
save_json(merged_json, output_json_file)

# Convert the merged JSON to CSV
json_to_csv(merged_json, output_csv_file)
