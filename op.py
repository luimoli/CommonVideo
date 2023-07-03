import os
from pathlib import Path

def copy_linux(file_path, save_folder):
    # file_path.replace('//', '/')
    # save_folder.replace('//', '/')
    print(file_path)
    print(save_folder)
    file_path = Path(file_path)
    save_folder = Path(save_folder)
    bash_command = f'cp -r {file_path} {save_folder}'
    os.system(bash_command)
    # print(f'from {file_path} to {save_folder / file_path.name}: copy success!')
    # print(f'copy success!')


def copy_select_linux(file_root, save_root):
    file_root = Path(file_root)
    files = [f for f in file_root.iterdir() if f.is_file()]
    target_name_list = [str(i).zfill(3) for i in range(1, 9)]
    for file in files:
        if file.name[:3] in target_name_list:
            copy_linux(file, save_root)



if __name__ == '__main__':
    # file_path = r"/home/mengmengliu/datasets/Tests/test_LQ_img/test_1"


    file_root = r'/dataset2/oldanime_smore/clips/'
    save_folder = r'/data/媒体PoC/temp/反交错_动画/'
    copy_select_linux(file_root, save_folder)