from glob import glob
import os
import random
import shutil
from pathlib import Path


def copy_video_python(file_path, save_folder):
    """from file_path to save_path's parent folder
    Args:
        file_path (_type_): _description_
        save_path (_type_): _description_
    """
    file_path = Path(file_path)
    save_folder = Path(save_folder)
    shutil.copy(file_path, save_folder / file_path.name)
    
    print(f'from {file_path} to {save_folder / file_path.name}: copy success!')

def copy_video_linux(file_path, save_folder):
    """from file_path to save_path's parent folder
    Args:
        file_path (_type_): _description_
        save_path (_type_): _description_
    """
    # file_path = Path(file_path)
    # save_folder = Path(save_folder)
    bash_command = f'cp -r {file_path} {save_folder}'
    os.system(bash_command)
    # print(f'from {file_path} to {save_folder / file_path.name}: copy success!')
    print(f'copy success!')


if __name__ == '__main__':
    file_path_list=[
        "/data/媒体PoC/20210322_高达 （日本）/02-初始视频/高达-20211216/inuyasha_S104_mono4st_SD_ProRESHQ_2997fps.mov",
        "/data/媒体PoC/20210322_高达 （日本）/02-初始视频/高達-20210322T052546Z-001/高達/犬夜叉_QT720DnxHR.mov",
        "/data/媒体PoC/20210322_高达 （日本）/02-初始视频/高達-20210322T052546Z-002/高達/rivaius_QT720DnxHR.mov",
        "/data/媒体PoC/20220513-东映动画/2-原始数据/神風怪盗ジャンヌ_ep01_SD_5994i_2ch_ProresHQ.mov",
        "/data/媒体PoC/20220806-手塚（日本）/02-原始数据/手潈/Leo2S1_ProresHQ.mov",
        "/data/媒体PoC/20220806-手塚（日本）/02-原始数据/手潈/LeoS1_ProresHQ.mov",
        "/data/媒体PoC/20220806-手塚（日本）/02-原始数据/手潈/AtomS114_ProresHQ.mov",
        "/data/媒体PoC/20220902-日本动漫/01-原始数据/papuwa_edit.mov",
        "/data/媒体PoC/20220905-日本东映数字/01-原始数据/restore_test_source_HQ.mov",
        "/data/媒体PoC/20221010-超时空要塞/01-原始数据/Macross_ai oboeteimasuka_UPcom TEST.mov",
        "/data/媒体PoC/20221010-超时空要塞/01-原始数据/Macross_ai oboeteimasuka_UPcom TEST-540.mov",
        "/data/媒体PoC/20221010-超时空要塞/01-原始数据/Macrossplus MOVIE_UPcom TEST.mov",
        "/data/媒体PoC/20221010-超时空要塞/01-原始数据/Macrossplus MOVIE_UPcom TEST-540.mov",
        "/data/媒体PoC/20221010-超时空要塞/01-原始数据/MacrossZero_ UPcom_test_Section1_044114_pulldown.mov",
        "/data/媒体PoC/20221010-超时空要塞/01-原始数据/MacrossZero_ UPcom_test_Section2_pulldown.mov"
    ]
    save_folder = Path(r"/dataset2/oldanime_smore/videos/")

    for i in range(len(file_path_list)):
        file_path = file_path_list[i]
        file_path = Path(file_path)
        save_name = str(i+1).zfill(3)+file_path.suffix

        bash_command = f'cp -r {file_path} {save_folder / save_name}'
        # os.system(bash_command)
        print(file_path)
        print(save_folder / save_name)

