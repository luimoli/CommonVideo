import imageio_ffmpeg
import json
import os
from decode_video import decode

if __name__ == '__main__':
    # in_reader = imageio_ffmpeg.read_frames(r'C:\Users\liumm\Videos\aaavideo\160825_05_Sunflowers3_1080p.mp4')

    file_path = '\\\\192.168.100.201\\MediaStore-share\\媒体PoC\\20221010-超时空要塞\\01-原始数据\\Macross_ai oboeteimasuka_UPcom TEST.mov'
    save_path = r'D:\Data\Videos\Macross\cut0.mov'
    # bash_command = f'ffmpeg -ss 00:00:02 -to 00:00:14 -i "{file_path}" -c:v copy -c:a copy "{save_path}"'
    bash_command = f'ffmpeg -i "{save_path}" -q:v 0 "{save_path[:-4]}.mp4"'
    # os.system(bash_command)


    file_path = r'D:\Data\Videos\Macross\cut3.mov'
    save_folder = r'D:\Data\Videos\Macross\cut3'
    decode(file_path, save_folder)
    