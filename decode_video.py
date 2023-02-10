from glob import glob
import os
import random

def decode(file_path, save_folder):
    if not os.path.exists(save_folder):os.makedirs(save_folder)
    bash_command = f'ffmpeg -i "{file_path}" -filter_complex "scale=in_color_matrix=bt709:in_range=limited" {save_folder}\%5d.png'
    os.system(bash_command)

def decode_as_folder(file_root, save_root):
    """_summary_
    Args:
        file_root (str): contain videos
        save_root (str): contrain folders with imgs.
    """
    if not os.path.exists(save_root):os.makedirs(save_root)

    file_paths = glob(f'{file_root}\\*')
    # print(len(file_paths))
    for file_path in file_paths:
        file_name = os.path.basename(file_path)[:-4]
        save_folder = os.path.join(save_root, file_name)
        if not os.path.exists(save_folder): os.makedirs(save_folder)
        decode(file_path, save_folder)

if __name__ == '__main__':
    # file_path = r'D:\Data\Videos\Macross\cut3.mov'
    # save_folder = r'D:\Data\Videos\Macross\cut3'
    # decode(file_path, save_folder)

    file_root = r"E:\home\mengmengliu\datasets\Tests\original_LQ_video"
    save_root = r"E:\home\mengmengliu\datasets\Tests\test_LQ_img"
    decode_as_folder(file_root, save_root)