import numpy as np
import json
import os
from pathlib import Path
from glob import glob

def rename_clips(folder_root, move_root, label_path, label_save_path, restart_number, zfill_num):
    """rename clip-folders from folder_root to move_root
    <folder_root>
        --<clip0>
            --00001.png
        --<clip1>
            --00001.png
    Args:
        folder_root (str): contains clip-folders
        label_path (str): the old label's path -> {'clipname':"{source:xxx, timestamp:xxxx}"}
        restart_number (int): rename from restart_number
        zfill_num (int): fill to 
    """
    root = Path(folder_root)
    mv_root = Path(move_root)
    subdirs = [d for d in root.iterdir() if d.is_dir()]
    sortdirs = sorted(subdirs)
    with open(label_path, 'r') as f:
        label_json = json.load(f)
    label = label_json
    for i in range(len(sortdirs)):
        folder_path = Path(sortdirs[i])
        new_key = str(restart_number + i).zfill(zfill_num)
        old_key = folder_path.name
        label[new_key] = label.pop(old_key)
        folder_path.rename(mv_root / new_key)

    with open(label_save_path,"w",encoding="utf-8") as f:
        json.dump(label, f)


def create_dataset_index(dataset_root):
    pass


if __name__ == '__main__':
    folder_root = r"D:\test_folder"
    move_root = r"D:\test_folder2"
    label_path = r'dataset_label\test.json'
    label_save_path = r'dataset_label\test_new.json'
    rename_clips(folder_root, move_root, label_path, label_save_path, restart_number=20, zfill_num=4)



    # clip_path_list = glob(folder_root, "/*")




# # 遍历当前工作目录下的所有文件夹
# dirs = [d for d in os.listdir(current_dir) if os.path.isdir(d)]

# # 根据文件夹名字中的数字进行排序
# dirs = sorted(dirs, key=lambda x: int(x.split('folder')[1]))

# # 遍历文件夹列表，重命名文件夹
# for i, d in enumerate(dirs):
#     new_name = 'folder{}'.format(i+1)
#     os.rename(d, new_name)


# if __name__ == '__main__':
#     label1 = r'dataset_label/clip_label.json'
#     label2 = r'dataset_label/clip_label_v1.json'

#     with open(label1, 'r') as f:
#             content1 = json.load(f)
            
#     with open(label2, 'r') as f:
#             content2 = json.load(f)



# new = {**content1, **content2}
# label_save_path = r'./clip_label_v1.json'
# with open(label_save_path,"w",encoding="utf-8") as f:
#         json.dump(new, f)

# # verify
# with open(label_save_path, 'r') as f:
#         total_label = json.load(f)
#         print(len(total_label))
#         print(total_label['0000'])