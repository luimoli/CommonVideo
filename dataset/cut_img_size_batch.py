import cv2
import os
import numpy as np
from glob import glob
from pathlib import Path


def CutAnimeSize(clips_root, new_clips_root, scale):
    for clip_folder in os.listdir(clips_root):
        clip_folder_path = os.path.join(clips_root, clip_folder)
        save_clip_folder_path = os.path.join(new_clips_root, clip_folder)
        if not os.path.exists(save_clip_folder_path): os.makedirs(save_clip_folder_path)
        if os.path.isdir(clip_folder_path):
            for img_name in os.listdir(clip_folder_path):
                img_path = os.path.join(clip_folder_path, img_name)
                img = cv2.imread(img_path)
                h, w, c = img.shape
                if h % scale > 0:
                    new_h  = h // scale * scale
                    cut = h - new_h
                    cut_from, cut_to = cut//2, h - (cut - cut // 2)
                    img = img[cut_from:cut_to, :, :].copy()
                if w % scale > 0:
                    new_w  = w // scale * scale
                    cut = w - new_w
                    cut_from, cut_to = cut//2, w - (cut - cut // 2)
                    img = img[:, cut_from:cut_to, :].copy()
                save_path = os.path.join(save_clip_folder_path, img_name)
                cv2.imwrite(save_path, img)
                



if __name__ =='__main__':
    clips_root = '/dataset/mengmengliu/AVC/lbo_training_data/real_world_video_to_train_lbo_3_original'
    new_clips_root = '/dataset/mengmengliu/AVC/lbo_training_data/real_world_video_to_train_lbo_3'
    CutAnimeSize(clips_root, new_clips_root, 16)