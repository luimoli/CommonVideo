import os, sys
import cv2
from glob import glob

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
    