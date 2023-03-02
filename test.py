import imageio_ffmpeg
import json
import os
from video_decode import decode
from utils.func import judge_number
import shutil

if __name__ == '__main__':
    # in_reader = imageio_ffmpeg.read_frames(r'C:\Users\liumm\Videos\aaavideo\160825_05_Sunflowers3_1080p.mp4')

    file_path = '\\\\192.168.100.201\\MediaStore-share\\媒体PoC\\20221010-超时空要塞\\01-原始数据\\Macross_ai oboeteimasuka_UPcom TEST.mov'
    save_path = r'D:\Data\Videos\Macross\cut0.mov'
    # bash_command = f'ffmpeg -ss 00:00:02 -to 00:00:14 -i "{file_path}" -c:v copy -c:a copy "{save_path}"'
    bash_command = f'ffmpeg -i "{save_path}" -q:v 0 "{save_path[:-4]}.mp4"'
    # os.system(bash_command)


    file_path = r'D:\Data\Videos\Macross\cut3.mov'
    save_folder = r'D:\Data\Videos\Macross\cut3'
    # decode(file_path, save_folder)


    # path = r'/home/mengmengliu/datasets/Tests/0212/test_cmp'
    # for folder in os.listdir(path):
    #     if judge_number(folder, (0,3)):
    #         folder_path = os.path.join(path, folder)
    #         for img in os.listdir(folder_path):
    #             if len(img[:-4]) == 4:
    #                 img_path = os.path.join(folder_path, img)
    #                 os.remove(img_path)
                    

    