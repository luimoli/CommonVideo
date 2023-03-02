from glob import glob
import os
import random
from pathlib import Path

def cut_video(file_path, save_path, time_from, time_to=None, time_duration=None):
    """_summary_

    Args:
        file_path (str): video path
        save_path (str): video path
        time_from (str): 00:05:40
        time_to (str, optional): _description_. Defaults to None.
        time_duration (int, optional): _description_. Defaults to None.
    """
    if (not time_to and time_duration) or (time_to and not time_duration):
        print(os.path.exists(file_path))
        if time_to:
            bash_command = f'ffmpeg -ss {time_from} -to {time_to} -i "{file_path}" -c:v copy -c:a copy "{save_path}"'
        elif time_duration:
            bash_command = f'ffmpeg -ss {time_from} -t {time_duration} -i "{file_path}" -c:v copy -c:a copy "{save_path}"'
        else:
            print('error!')
        os.system(bash_command)
    else:
        print('select one from time_to and time_duraiton')

if __name__ == '__main__':
    file_path = r'\\192.168.100.201\MediaStore-share\媒体PoC\20221010-超时空要塞\01-原始数据\Macrossplus MOVIE_UPcom TEST-540.mov'
    save_path = r'E:\home\mengmengliu\datasets\Tests\original_LQ_video\macross_1.mov'
    time_from = '00:00:37'
    time_to='00:00:45'
    time_duration=None
    cut_video(file_path, save_path, time_from, time_to, time_duration)