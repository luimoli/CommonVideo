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
    print(f'copy success!')



if __name__ == '__main__':
    file_path = r"/home/mengmengliu/datasets/Tests/test_LQ_img/test_1"
    save_folder = r"/dataset2/oldanime_smore/images/smpte_170m"
    copy_linux(file_path, save_folder)