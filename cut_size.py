import os, sys
import cv2
from glob import glob
from pathlib import Path

def detect_folder_and_cut(clipimg_root, factor=4):
    """
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
    for folder in folders:
        files = [f for f in folder.iterdir() if f.is_file()] # frames' path lists
        assert len(files) > 0
        first_img = cv2.imread(str(files[0]))
        h, w, c = first_img.shape

        if h % factor or w % factor: # h or w is not multiple of factor 
            hnew = h - h % factor
            wnew = w - w % factor
            for img_path in files:
                img = cv2.imread(str(img_path))
                img_new = img[:,:,:].copy()
                cv2.imwrite(img_path, img_new)
        else:
            print(folder, '  meets the requirement!')






def cut_img_to_fit_size(folder_root):
    for folder in os.listdir(folder_root):
        folder_path = os.path.join(folder_root, folder)
        if os.path.isdir(folder_path):
            if judge_number(folder, (6,11)): #TODO
                print(folder_path)
                __cut_img(folder_path)


def __cut_img(folder_path):
    img_path_list = glob(folder_path+'/*')
    for img_path in img_path_list:
        img = cv2.imread(img_path)
        img_cut = img[1:485, :, :].copy()
        save_folder = folder_path+'_cut'
        if not os.path.exists(save_folder):os.makedirs(save_folder)
        cv2.imwrite(os.path.join(save_folder, os.path.basename(img_path)), img_cut)


def judge_number(file_path, number_range):
    name_list = [str(i) for i in range(number_range[0], number_range[1], 1)]
    for i in name_list:
        if i in file_path:
            return True
    return False

if __name__ == '__main__':
    folder_root = "/home/mengmengliu/datasets/Tests/test_LQ_img/"
    cut_img_to_fit_size(folder_root)
    