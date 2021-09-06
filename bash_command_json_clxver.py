import os
import glob
import argparse
import json
from multiprocessing import Pool
# from tqdm import tqdm
import glob
import cv2

import numpy as np
# import pandas as pd
# from openpyxl import load_workbook
from PIL import Image
# from ffprobe import FFProbe
from videoprops import get_video_properties
import shutil
def _filter_file(rootPath, json_data, localRoot, saveRoot, keyword=""):
    # input("check  HLLL")

    data_list2 = []

    with open(json_data, 'r') as f:
        data_list = json.load(f)

    count = 0
    for data in data_list:
        hr_url_remote =  data[keyword[0]]

        attriHr = hr_url_remote.split('/')
        video_name = attriHr[-1]
        savePath = os.path.join(saveRoot,video_name)
        savePath = os.path.join(saveRoot,video_name)
        # bash_commend = "rsync -r"  -r -a :subfolder. recursively

        # input("check")
        hr_url =  os.path.join(localRoot,video_name)

        if  os.path.exists(hr_url):
            hr_url = "\"" + hr_url + "\""  # vide name with space " " should add quotes to the pash
            savePath = "\"" + savePath + "\""

            if "sport" in hr_url_remote :
                print("{}_{}_=========".format(count, video_name))

                bash_commend = "mv "  + hr_url +" " + savePath
                os.system(bash_commend)
                count +=1


def _rsync_file_copy(rootPath, json_data, saveRoot, keyword=""):
    # input("check  HLLL")

    data_list2 = []

    with open(json_data, 'r') as f:
        data_list = json.load(f)

    count = 0
    for data in data_list:
        hr_url =  data[keyword[0]]

        attriHr = hr_url.split('/')
        video_name = attriHr[-1]
        savePath = os.path.join(saveRoot,video_name)
        savePath = os.path.join(saveRoot,video_name)
        # bash_commend = "rsync -r"  -r -a :subfolder. recursively

        print("{}_{}_=========".format(count,video_name))
        # input("check")
        hr_url = "\""  + hr_url + "\""         # vide name with space " " should add quotes to the pash
        savePath = "\""  + savePath + "\""



        bash_commend = "rsync -P "  + hr_url +" " + savePath
        os.system(bash_commend)
        count +=1

def _xml_file_ffmpeg(rootPath, xml, saveRoot, keyword=""):
    # input("check  HLLL")

    data_list2 = []

    with open(json_data, 'r') as f:
        data_list = json.load(f)

    count = 0
    for data in data_list:
        hr_url =  data[keyword[0]]

        attriHr = hr_url.split('/')
        video_name = attriHr[-1]
        savePath = os.path.join(saveRoot,video_name)
        savePath = os.path.join(saveRoot,video_name)
        # bash_commend = "rsync -r"  -r -a :subfolder. recursively

        print("{}_{}_=========".format(count,video_name))
        # input("check")
        hr_url = "\""  + hr_url + "\""         # vide name with space " " should add quotes to the pash
        savePath = "\""  + savePath + "\""



        bash_commend = "rsync -P "  + hr_url +" " + savePath
        os.system(bash_commend)
        count +=1

def read_xlsx(rootPath, xml_path):
    print("De")
    wb = wb = load_workbook(xml_path, read_only=True)
    print(wb.sheetnames)
    ws = wb.get_sheet_by_name('Nature_20201013')
    path_name  = 0
    start_hh = 1
    start_mm = 2
    start_ss = 3
    end_hh   = 4
    end_mm   = 5
    end_ss   = 6
    path_ = np.array([r[path_name].value for r in ws.iter_rows()])

    start_hh_list = np.array([r[start_hh].value for r in ws.iter_rows()])
    start_mm_list = np.array([r[start_mm].value for r in ws.iter_rows()])
    start_ss_list = np.array([r[start_ss].value for r in ws.iter_rows()])

    end_hh_list   = np.array([r[end_hh].value for r in ws.iter_rows()])
    end_mm_list   = np.array([r[end_mm].value for r in ws.iter_rows()])
    end_ss_list  = np.array([r[end_ss].value for r in ws.iter_rows()])

    saveFolder = os.path.join(rootPath,"clip_UHD_4k/Nature_20201013")

    for idx in range( len(path_)):
        i = idx + 1
        path_full = os.path.join(rootPath, path_[i])
        path_full.replace("//","\\")
        attriHr = path_full.split('\\')
        start_hms = start_hh_list[i] + "_"+ start_mm_list[i] + "_"+ start_ss_list[i]
        end_hms = end_hh_list[i] + "_"+ end_mm_list[i] + "_"+ end_ss_list[i]

        start_hms_ = start_hh_list[i] + ":"+ start_mm_list[i]  + ":"+ start_ss_list[i]
        end_hms_ = end_hh_list[i]  + ":"+ end_mm_list[i] + ":" + end_ss_list[i]


        video_name =  attriHr[-1]
        new_name = video_name.split(".")[0]
        format_  = video_name.split(".")[1]
        new_name_ = new_name +"_" +start_hms + "_" + end_hms +'.' +format_;

        save_path_full = os.path.join(saveFolder, new_name_)

        path_full_ = "\"" + path_full + "\""  # vide name with space " " should add quotes to the pash
        save_path_full_ = "\"" + save_path_full + "\""

        bash_commend = "ffmpeg -i {} -ss {} -to {} -c:v libx264 -crf 0 {}".format(path_full_, start_hms_, end_hms_, save_path_full_)
        os.system(bash_commend)

        print(path_full)

        print(save_path_full)

def file_name(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir, topdown=False):
        for name in files:
            L.append(os.path.join(root, name))

        L.append(root)

    return L

def merge_img_to_video(img_path, video_save_path):
    bash_commend = "ffmpeg -i" + "  " + "\"" + img_path + "\"" +  "  " + "\"" + out_path + "/" + "%7d.png" + "\""

    os.system(bash_commend)

def dump_video_frame_folder_ffmpeg(video_root, save_root):
    """
        rootPath = "/home/data2/temp/effect/ViQuali_TestSet"
        save_path = "/home/data2/temp/effect/ViQuali_TestSet_frame"
        dump_video_frame_folder_ffmpeg(rootPath, save_path)
    """

    in_list = file_name(video_root)

    for in_url in in_list:
        for video_fp in os.listdir(in_url):
            if 'mkv' in video_fp or 'mp4' in video_fp or 'webm'  or 'mov'in video_fp:
                attris = video_fp.split('.')
                out_path = os.path.join( in_url.replace(video_root, save_root),  "{}".format(attris[0]) )

                if not os.path.exists( out_path):
                    os.makedirs(out_path)

                # print("{}_{}_=========".format(out_path, video_fp ))
                # path string should be "path_url"
                bash_commend = "ffmpeg -i"+ "  "       +         "\"" + in_url +"/"+ video_fp +  "\""+ "  "       +         "\""  + out_path + "/" + "%7d.png" +  "\""

                os.system(bash_commend)


    print("Hello world")


def merges_frame_video_ffmpeg(img_root, save_root,framerate):
    """
        rootPath = "/home/data2/temp/effect/ViQuali_TestSet"
        save_path = "/home/data2/temp/effect/ViQuali_TestSet_frame"
        merges_frame_video_ffmpeg(rootPath, save_path)
    """

    for img_fp in os.listdir(img_root):
        img_path = os.path.join(img_root,img_fp)
        img = cv2.imread(img_path)
        h,w,c = img.shape
        if not os.path.exists(save_root):
            os.makedirs(save_root)
        break

    attris = img_root.split("/")

    bash_commend = "ffmpeg  -r {} -i  {}/%7d.png -c:v libx264   -crf 0 {}/{}.mp4".format(
                                             framerate, img_root,save_root ,attris[-1] )

    os.system(bash_commend)


    print("Hello world")


def common_ffmpeg(video_root, save_root):
    """
        rootPath = "/home/data2/temp/effect/ViQuali_TestSet"
        save_path = "/home/data2/temp/effect/ViQuali_TestSet_frame"
        merges_frame_video_ffmpeg(rootPath, save_path)
    """

    if not os.path.exists(save_root):
        os.makedirs(save_root)
    for video_fp in os.listdir(video_root):
        if 'mkv' in video_fp or 'mp4' in video_fp or 'webm'  or 'mov'in video_fp:
            attris = video_fp.split('.')

            # print("{}_{}_=========".format(out_path, video_fp ))
            # path string should be "path_url"
            video_path = video_root + "/" + video_fp
            out_path   = save_root + "/" + video_fp
            # metadata = FFProbe(video_path)
            props = get_video_properties(video_path)

            h = props['height']
            ratio = float(props['height']) / h

            ratio = 1.0
            h     = int(float(props['height']) * ratio)
            w     = int(float(props['width']) * ratio)

            # w     = int(float(props['width']) / ratio)
            # bash_commend = "ffmpeg -i {}  {}/%7d.png  ".format(video_path ,out_path)
            bash_commend = "ffmpeg -i {} {} {}  ".format(video_path,"-c:v libx264  -pix_fmt yuv444 -crf 0 out_ex1.mp4" ,out_path)

            os.system(bash_commend)


    print("Hello world")

def pure_ffmpeg():

    bash_commend = "ffmpeg -i {} {} {}  ".format(r"F:\POC\qianShiTong\压缩超分_org\监控图_压缩\监控图__quality30.mp4",
                                                 r"F:\POC\qianShiTong\压缩超分_org\监控图_压缩\监控图__quality30"
                                                 )

    os.system(bash_commend)

def renameIdx(buff_dir, out):
    if not os.path.exists(out):
        os.mkdir(out)

    picName_list = sorted(os.listdir(buff_dir))

    idx = 1
    for video_fp in picName_list:
        if 'png' or "JPEG" or "jpg" in video_fp:
            video_format = 'jpg'
            attri = video_fp.split('.')

            # video_fp_new = "{}.png".format(str(idx).zfill(7))

            # img = cv2.imread(os.path.join(buff_dir, video_fp), -1)
            print(video_fp)
            writePath = '{}.{}'.format(str(idx).zfill(7),video_format)
            # os.rename(os.path.join(buff_dir, video_fp), os.path.join(buff_dir, writePath))

            # cv2.imwrite(os.path.join(out , writePath), img);
            shutil.copy(os.path.join(buff_dir, video_fp), os.path.join(out , writePath))
            idx +=1

if __name__=='__main__':
    #TODO 1: 视频到图片
    # common_ffmpeg(video_root, save_root)

    #TODO 2： 删除neat里面的图片，然后重新 排序命名
    # renameIdx("/home/data2/temp/merge_5s", "/home/data2/temp/merge_5s_out")

    #TODO 3: 输入图片文件夹的路径输入
    # common_ffmpeg(video_root, save_root)
    ## ffmpeg -framerate 10 -i %7d.png -c:v libx264rgb -crf 0 output.mp4


    # #=============  dump video ========================
    
    rootPath = "/home/user/liumengmeng/VideoAlgoToolChain/denoise_Test"  #多个视频 的根路径
    # rootPath = 'D:/Data_Denoise/denoise_Test/'
    save_path = '/home/user/liumengmeng/VideoAlgoToolChain/denoise_Test_PNG'
    dump_video_frame_folder_ffmpeg(rootPath, save_path)
    # #=============  dump video ========================


    # ================   save folder ======================
    # file_list = file_name(rootPath)
    # for in_url in file_list:
    #     merges_frame_video_ffmpeg(in_url,save_path,rate)
















    # # #=============   video split ========================
    #
    # rootPath = r"F:\POC\qianShiTong\720P_2M\720P_2M_SR"
    # save_path = r"F:\POC\qianShiTong\720P_2M\720P_2M_SR_2M"
    # common_ffmpeg(rootPath, save_path)
    # # #=============   video ========================

    # ================   save folder ======================







