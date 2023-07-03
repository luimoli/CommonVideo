# import glob
# import cv2
import os

from pathlib import Path


def get_file_Iterator(path):
    if not isinstance(path, Path):
        path = Path(path)
    files = [x for x in path.rglob('*') if x.is_file()]
    return files

def get_folder_Iterator(rootDir, item_list, dir_list, abspath_list):
    '''
    this suits the sub-folder situation:
    get abs-path of each file(including the subfolder)
    --------------------------------------------------
    rootDir: root path
    item_list: file_name 's list
    dir_list: the latest folder path for each file_name
    abspath_list: absolute path for each file_name
    --------------------------------------------------
    '''
    for file_name in os.listdir(rootDir): 
        path = os.path.join(rootDir, file_name) 
        if os.path.isdir(path): 
            get_folder_Iterator(path,item_list, dir_list, abspath_list)
        else:
            # print(path)
            # print(rootDir)
            # print(file_name)
            item_list.append(file_name)
            dir_list.append(rootDir)
            abspath_list.append(path)
    return item_list,dir_list, abspath_list



if __name__=='__main__':
    video_root = '/home/user/liumengmeng/VideoAlgoToolChain/denoise_Test'
    save_root = '/home/user/liumengmeng/VideoAlgoToolChain/denoise_Test_PNG'

    item_list, dir_list, abspath_list = [], [], []
    rootDir = r"D:\Data\Videos\动漫_gt"
    item_list,dir_list, abspath_list = get_folder_Iterator(rootDir, item_list, dir_list, abspath_list)
    print(abspath_list)
