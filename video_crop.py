from glob import glob
import os
import random
import shutil
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

def copy_video(file_path, save_path):
    """from file_path to save_path's parent folder
    Args:
        file_path (_type_): _description_
        save_path (_type_): _description_
    """
    save_pth = Path(save_path)
    save_stem = save_pth.parent
    # print(save_stem)
    bash_command = f'cp -r {file_path} {save_stem}'
    os.system(bash_command)
    # shutil.copy
    
    print(f'from {file_path} to {save_stem}: copy success!')

if __name__ == '__main__':
    file_path = Path(r"/dataset2/oldanime_smore/original_videos/015.mov")
    save_path = r"/dataset2/oldanime_smore/clips/" + file_path.stem + '_01' + file_path.suffix
    # print(save_path)
    time_from = '00:03:11'

    # time_to='00:00:19.979'
    time_to=None

    time_duration='00:00:30'
    # time_duration=None

    cut_video(str(file_path), save_path, time_from, time_to, time_duration)
    # copy_video(file_path, save_path)
    
