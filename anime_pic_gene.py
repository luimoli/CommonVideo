from glob import glob
import os
from pickle import TRUE
import random
from tqdm import tqdm
import math
import json
import subprocess

def decode(file_path, save_folder):
    if not os.path.exists(save_folder):os.makedirs(save_folder)
    bash_command = f'ffmpeg -i "{file_path}" -filter_complex "scale=in_color_matrix=bt709:in_range=limited" {save_folder}\%4d.png'
    os.system(bash_command)



def decode_as_folder(file_root, save_root):
    if not os.path.exists(save_root):os.makedirs(save_root)

    file_paths = glob(f'{file_root}\\*.mp4')
    # print(len(file_paths))
    for file_path in file_paths:
        file_name = os.path.basename(file_path)[:-4]
        save_folder = os.path.join(save_root, file_name)
        if not os.path.exists(save_folder): os.makedirs(save_folder)
        decode(file_path, save_folder)


if __name__ == '__main__':
    file = r"\\192.168.100.201\Media-Dev\Video_Depo\动漫\Fate stay night UBW\[Kamigami] Fate stay night UBW - 16 [1080p x265 Ma10p FLAC Sub(Eng,Jap)].mkv"
    save_folder = r"\\192.168.100.201\Media-Dev\Video_Depo\动漫\lmm\720p\nonstop_img"
    # decode(file_path=file,save_folder=save_folder)

    file_root = r'\\192.168.100.201\Media-Dev\Video_Depo\动漫\Anime_Dataset\1080p'
    save_root = r'\\192.168.100.201\Media-Dev\Video_Depo\动漫\Anime_Dataset\1080p_pic'
    decode_as_folder(file_root, save_root)