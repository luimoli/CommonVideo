import cv2
import numpy as np
import imageio_ffmpeg
import os

INPUT_FILE1 = '/home/user/liumengmeng/VideoAlgoToolChain/atest/original.mp4'
INPUT_FILE2 = '/home/user/liumengmeng/VideoAlgoToolChain/atest/FDN-raw001--denoise_标清采访clip1_720x576p-420.mp4'
OUTPUT_FILE = '/home/user/liumengmeng/VideoAlgoToolChain/atest/merge.mp4'


def merge_two_video(INPUT_FILE1, INPUT_FILE2,OUTPUT_FILE):
    '''

    '''
    reader1 = cv2.VideoCapture(INPUT_FILE1)
    reader2 = cv2.VideoCapture(INPUT_FILE2)
    width = int(reader1.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(reader1.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(reader1.isOpened())
    print(reader2.isOpened())
    c = 0
    vw_pure = None
    vw_pure = imageio_ffmpeg.write_frames(OUTPUT_FILE,
                                        (width * 2, height),
                                        fps=25,
                                        pix_fmt_out='yuv420p',
                                        # pix_fmt_out='yuv420p10le',
                                        quality=10,
                                        ffmpeg_timeout=0,  # libx264 in default
                                        macro_block_size=1)
    vw_pure.send(None)

    while reader1.isOpened() and reader2.isOpened():
        ret1, frame1 = reader1.read()
        ret2, frame2 = reader2.read()
        if ret1 and ret2:
            out_frame = np.concatenate((frame1, frame2), axis=1)
            # vw_pure.send(out_frame)
            tmp_cat = out_frame[:, :, ::-1].copy() # 转换BGR RGB
            vw_pure.send(tmp_cat)
        else:
            break

    vw_pure.close()
    reader1.release() 
    reader2.release()
    cv2.destroyAllWindows()



if __name__=='__main__':
    ori_root = '/home/user/liumengmeng/CommonVideo/denoise_cmp_v2/NoisyInput'
    out_root = '/home/user/liumengmeng/CommonVideo/denoise_cmp_v2/NoiseData_output'
    cmp_root = '/home/user/liumengmeng/CommonVideo/denoise_cmp_v2/cmp_result_v2_10bit'
    if not os.path.exists(cmp_root):os.makedirs(cmp_root)


    # for item in os.listdir(out_root):
    #     ori_path = os.path.join(ori_root, item)
    #     out_path = os.path.join(out_root, item)
    #     cmp_save_path = os.path.join(cmp_root, item)
    #     merge_two_video(ori_path, out_path,cmp_save_path)


    for item_clx in os.listdir(out_root):
        # import ipdb;ipdb.set_trace()
        attris = item_clx.split('.')
        item = attris[0][:-8]
        ori_path = os.path.join(ori_root, item+'.'+attris[1])
        out_path = os.path.join(out_root, item_clx)
        cmp_save_path = os.path.join(cmp_root, item_clx)
        merge_two_video(ori_path, out_path,cmp_save_path)