import os, sys
import cv2
from glob import glob
from pathlib import Path

def detect_folder_and_cutframes(clipimg_root, factor=8):
    """
    frame'shape :h or w should be multiple of factor, or clipped to fit.
    clipimg_root
        --clip_1
            --0001.png
            --0002.png
    Args:
        clipimg_root (_type_): _description_
        factor: frame resolution h and w should be multiple of factor
    """
    root = Path(clipimg_root)
    folders = [f for f in root.iterdir() if f.is_dir()]
    folders = sorted(folders)
    for folder in folders:
        files = [f for f in folder.iterdir() if f.is_file()] # frames' path lists
        assert len(files) > 0
        first_img = cv2.imread(str(files[0]))
        h, w, c = first_img.shape

        # if h % factor or w % factor: # h or w is not multiple of factor 
        if (h % factor or w % factor) and h < 500: #TODO h or w is not multiple of factor  |and| only operate those under 540p

            for img_path in files:
                img = cv2.imread(str(img_path))
                img_new = img[h%factor//2 + h%factor%2 : h-h%factor//2, w%factor//2+ w%factor%2 : w-w%factor//2, :].copy()
                # print(img_new.shape)
                cv2.imwrite(str(img_path), img_new)

            print(folder, '  cut fullfilled!')
        else:
            print(folder, '  meets the requirement!')



if __name__ == '__main__':
    # folder_root = "/dataset2/oldanime_smore/images/smpte_170m"
    folder_root = "/dataset2/oldanime_smore/images/709_709_709"
    
    detect_folder_and_cutframes(folder_root)
    