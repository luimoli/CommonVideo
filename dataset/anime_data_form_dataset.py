from glob import glob
import numpy as np
import sys
import os
import shutil
import random


def extract(path_ori, path_target, extract_num, extract_percent=None):
    """randomly extract clip-folders from path_ori to path_target
    Args:
        path_ori (str): _description_
        path_target (str): _description_
        extract_num (int): _description_
        extract_percent (float, optional): if this is defined, it will be prior to 'extract_num'. Defaults to None.
    """
    if extract_percent:
        extract_num = int(clip_num * extract_percent)

    if not os.path.exists(path_target): os.makedirs(path_target)
    clips_path_list = glob(path_ori + '*') 
    clip_num = len(clips_path_list) # num = num of clips in root_folder

    # # index the clip-folders by num:
    seq = range(0, clip_num)
    extract_index = random.sample(seq, extract_num)
    
    for i in range(clip_num):
        if i in extract_index:
            shutil.move(clips_path_list[i], path_target)


if __name__ == '__main__':
    
    # clip_num = 895
    # extract_index = np.random.randint(0, clip_num, (extract_num))

    path_ori = './AnimeDataset/'
    path_target = './val/'
    extract_num = 0
    extract(path_ori, path_target, extract_num)

    
    # for index in extract_index:
    #     clip_index = str(index).zfill(3)
    #     clip_path = os.path.join(path_ori, clip_index)
    #     shutil.move(clip_path, path_target)
