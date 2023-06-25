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
    file_path = r"/dataset2/oldfilm_smore/videos/016.mp4"
    save_path = r"/dataset2/oldfilm_smore/clips/016_01.mp4"
    time_from = '00:00:04'

    # time_to='00:00:00.919'
    time_to=None

    time_duration='00:00:30'
    # time_duration=None

    # cut_video(file_path, save_path, time_from, time_to, time_duration)
    copy_video(file_path, save_path)
    
    file_path_list=[
        "\\192.168.100.201\MediaStore-share\媒体PoC\20210322_高达 （日本）\02-初始视频\高达-20211216\inuyasha_S104_mono4st_SD_ProRESHQ_2997fps.mov",
        "\\192.168.100.201\MediaStore-share\媒体PoC\20210322_高达 （日本）\02-初始视频\高達-20210322T052546Z-001\高達\犬夜叉_QT720DnxHR.mov",
        "\\192.168.100.201\MediaStore-share\媒体PoC\20210322_高达 （日本）\02-初始视频\高達-20210322T052546Z-002\高達\rivaius_QT720DnxHR.mov",
        "\\192.168.100.201\MediaStore-share\媒体PoC\20220513-东映动画\2-原始数据\神風怪盗ジャンヌ_ep01_SD_5994i_2ch_ProresHQ.mov",
        "\\192.168.100.201\MediaStore-share\媒体PoC\20220806-手塚（日本）\02-原始数据\手潈\Leo2S1_ProresHQ.mov",
        "\\192.168.100.201\MediaStore-share\媒体PoC\20220806-手塚（日本）\02-原始数据\手潈\LeoS1_ProresHQ.mov",
        "\\192.168.100.201\MediaStore-share\媒体PoC\20220806-手塚（日本）\02-原始数据\手潈\AtomS114_ProresHQ.mov",
        "\\192.168.100.201\MediaStore-share\媒体PoC\20220902-日本动漫\01-原始数据\papuwa_edit.mov",
        "\\192.168.100.201\MediaStore-share\媒体PoC\20220905-日本东映数字\01-原始数据\restore_test_source_HQ.mov",
        "\\192.168.100.201\MediaStore-share\媒体PoC\20221010-超时空要塞\01-原始数据\Macross_ai oboeteimasuka_UPcom TEST.mov",
        "\\192.168.100.201\MediaStore-share\媒体PoC\20221010-超时空要塞\01-原始数据\Macross_ai oboeteimasuka_UPcom TEST-540.mov",
        "\\192.168.100.201\MediaStore-share\媒体PoC\20221010-超时空要塞\01-原始数据\Macrossplus MOVIE_UPcom TEST.mov",
        "\\192.168.100.201\MediaStore-share\媒体PoC\20221010-超时空要塞\01-原始数据\Macrossplus MOVIE_UPcom TEST-540.mov",
        "\\192.168.100.201\MediaStore-share\媒体PoC\20221010-超时空要塞\01-原始数据\MacrossZero_ UPcom_test_Section1_044114_pulldown.mov",
        "\\192.168.100.201\MediaStore-share\媒体PoC\20221010-超时空要塞\01-原始数据\MacrossZero_ UPcom_test_Section2_pulldown.mov"
    ]