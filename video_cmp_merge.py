from glob import glob
import os, sys
import numpy as np
import cv2

from bash_cmd_video import merges_frame_video_ffmpeg
from utils.func import judge_number


class CmpVideo():
    def __init__(self, ori_root, out_all_root) -> None:
        self.ori_root = ori_root
        self.out_all_root = out_all_root
        self.out_root = os.path.join(os.path.dirname(self.out_all_root), 'test_HQ_img')
        self.merge_root = os.path.join(os.path.dirname(self.out_all_root), 'test_cmp')
        # self.merge_video_root = os.path.join(os.path.dirname(self.merge_root), 'test_cmp_video')
        # self.out_video_root = os.path.join(os.path.dirname(self.out_root), 'test_HQ_video')
        self.makedir()
        self.generate_subfolder(self.ori_root, self.out_root, self.merge_root)

    def makedir(self):
        dir_list = [self.out_all_root, self.out_root, self.merge_root]
        for dir in dir_list:
            if not os.path.exists(dir): os.makedirs(dir)

    def generate_subfolder(self, ori_root, out_root, merge_root):
        for folder_name in os.listdir(ori_root):
            # ori_folder = os.path.join(ori_root, folder_name)
            out_folder_out = os.path.join(out_root, folder_name)
            out_folder_merge = os.path.join(merge_root, folder_name)
            if not os.path.exists(out_folder_out): os.makedirs(out_folder_out)
            if not os.path.exists(out_folder_merge): os.makedirs(out_folder_merge)

    def generate_merge_pic(self):
        for folder_name in os.listdir(self.ori_root):
            cmp1_folder = os.path.join(self.ori_root, folder_name)
            cmp2_folder = os.path.join(self.out_root, folder_name)
            merge_folder = os.path.join(self.merge_root, folder_name)

            if os.listdir(cmp2_folder) and judge_number(cmp2_folder, (0, 3)): #TODO
            # if os.listdir(cmp2_folder):
                print(f'==={merge_folder}===')
                self.__merge_pic(cmp1_folder, cmp2_folder, merge_folder)

    def __merge_pic(self, cmp1_folder, cmp2_folder, merge_folder):
        """_summary_
        Args:
            cmp1_folder (str): original img
            cmp2_folder (str): sr img
        Returns:
            _type_: _description_
        """
        
        cmp1_path_list = glob(cmp1_folder + '/*')
        cmp2_path_list = glob(cmp2_folder + '/*')
        cmp1_path_list = sorted(cmp1_path_list)
        cmp2_path_list = sorted(cmp2_path_list)
        assert len(cmp1_path_list) == len(cmp2_path_list)
        for i in range(len(cmp1_path_list)):
            img1 = cv2.imread(cmp1_path_list[i])
            img2 = cv2.imread(cmp2_path_list[i])
            img1_upscale = cv2.resize(img1, (img2.shape[1], img2.shape[0]), interpolation=cv2.INTER_CUBIC)
            assert img1_upscale.shape == img2.shape
            img_merge = np.concatenate((img1_upscale, img2), axis=1)

            save_path = os.path.join(merge_folder, os.path.basename(cmp1_path_list[i]))
            cv2.imwrite(save_path, img_merge)
    

    def encode_cmp_video(self):
        # lst = glob(self.merge_root + '/*')
        # for path in lst:
        #     if os.path.isdir(path):
        merges_frame_video_ffmpeg(self.merge_root, self.merge_root, 23.976)
    
    def encode_HQ_video(self):
        # lst = glob(self.merge_root + '/*')
        # for path in lst:
        #     if os.path.isdir(path):
        merges_frame_video_ffmpeg(self.out_root, self.out_root, 23.976)


if __name__ == '__main__':
    # cmp1_folder = r"C:\Users\liumm\Pictures\tst1"
    # cmp2_folder = r"C:\Users\liumm\Pictures\tst2"
    # res = merge_pic(cmp1_folder, cmp2_folder)
    # cv2.imwrite('./test.jpg', res)


    ori_root = "/home/mengmengliu/datasets/Tests/test_LQ_img/" # test videos'(imgs') root
    out_all_root = "/home/mengmengliu/datasets/Tests/v0_1/"
    # out_root = "/home/mengmengliu/datasets/Tests/0212/test_HQ_img/" # test SR results(SR imgs 
    # merge_root = "/home/mengmengliu/datasets/Tests/0212/test_cmp/" #  test SR results (cmp imgs)

    merge = CmpVideo(ori_root, out_all_root) ## generate_folders
    # merge.generate_merge_pic()
    # merge.encode_cmp_video()
    merge.encode_HQ_video()



