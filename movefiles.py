import os
import shutil
import re

def move_files(base_path="."):
    for filename in os.listdir(base_path):
        match = re.match(r"(\d+)[._](.*)", filename)
        if match:
            file_number = int(match.group(1))
            for i in range(1, 4001, 100):
                if i <= file_number <= i + 99:
                    folder_name = f"{i}-{i+99}"
                    folder_path = os.path.join(base_path, folder_name)
                    file_path = os.path.join(base_path, filename)
                    new_file_path = os.path.join(folder_path, filename)
                    shutil.move(file_path, new_file_path)
                    print(f"Moved {filename} to {folder_path}")
                    break

if __name__ == "__main__":
    move_files()