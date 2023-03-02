from glob import glob
import os
import random

def decode_video(file_path, save_folder):
    if not os.path.exists(save_folder):os.makedirs(save_folder)
    bash_command = f'ffmpeg -i "{file_path}" -filter_complex "scale=in_color_matrix=bt709:in_range=limited" {save_folder}/%5d.png'
    os.system(bash_command)

def decode_videos_as_folder(file_root, save_root):
    """_summary_
    Args:
        file_root (str): contain videos
        save_root (str): contrain folders with imgs.
    """
    if not os.path.exists(save_root):os.makedirs(save_root)

    file_paths = glob(f'{file_root}/*')

    for file_path in file_paths:
        if os.path.isfile(file_path):
            file_name = os.path.basename(file_path)[:-4]

            if judge_number(file_name, (0,3)):  # TODO
                print(file_path)
                save_folder = os.path.join(save_root, file_name)
                if not os.path.exists(save_folder): os.makedirs(save_folder)
                decode_video(file_path, save_folder)

def judge_number(file_path, number_range):
    name_list = [str(i) for i in range(number_range[0], number_range[1], 1)]
    for i in name_list:
        if i in file_path:
            return True
    return False



if __name__ == '__main__':
    # file_path = r'D:\Data\Videos\Macross\cut3.mov'
    # save_folder = r'D:\Data\Videos\Macross\cut3'
    # decode(file_path, save_folder)

    file_root = r"/home/mengmengliu/datasets/Tests/original_LQ_video/"
    save_root = r"/home/mengmengliu/datasets/Tests/test_LQ_img/"
    decode_videos_as_folder(file_root, save_root)