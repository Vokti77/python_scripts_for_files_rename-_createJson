import os
import json

def create_json_file(clothes_original_dir, clothes_dir, clothes_mask_dir, output_file):
    json_data = []

    for file_name in os.listdir(clothes_original_dir):
        if file_name.endswith('.png'):
            image_name = file_name.split('.')[0]
            # image_id = int(file_name.split('_')[1].split('.')[0])
            image_path = os.path.join(file_name)

            json_entry = {
                "id": image_name,
                "clothes_original": image_path,
                "clothes": os.path.join( f"{image_name}.jpg"),
                "clothes_mask": os.path.join(f"{image_name}.jpg"),
                "sleeves": "half",
                "length": "full",
                "ckpt": "0",
                "category": "tshirt"
            }

            json_data.append(json_entry)

    sorted_json_data = sorted(json_data, key=lambda x: (x['id'], x['clothes_original']))

    with open(output_file, 'w') as f:
        json.dump(sorted_json_data, f, indent=4)

if __name__ == "__main__":
    clothes_original_dir = input("Enter the directory name for clothes_original (.png format): ")
    clothes_dir = input("Enter the directory name for clothes (.jpg format): ")
    clothes_mask_dir = input("Enter the directory name for clothes_mask (.jpg format): ")

    output_file = "tanktop.json"
    create_json_file(clothes_original_dir, clothes_dir, clothes_mask_dir, output_file)

    print(f"JSON file {output_file} has been created.")
