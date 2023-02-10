import os
import random


def dump_video_frame_folder_ffmpeg(video_root, save_root, decode_type='709', platform ='win'):
    '''
    create VideoPNGs by seperate folders named by original filename each.
    -----------------------------------------------------------------------------------------------
    video_root: folder which contains multiple videos 
    save_root: which to save the video-frame-imgs, but should generate many sub-folders containing frame pngs
    -----------------------------------------------------------------------------------------------
    ---video_root
        ---video1.mp4
        ---video2.mkv
        ...
    ---save_root
        ---<video1>
        ---<video2>
    '''
    for item in os.listdir(video_root):
        video_path = os.path.join(video_root,item)
        if 'mkv' in item  or  'mp4' in item  or 'webm' in item or 'mov' or 'mxf' in item:
            attris = item.split('.')
            folder_path_namedbyvideo = os.path.join(save_root,attris[0])
            if not os.path.exists(folder_path_namedbyvideo):os.makedirs(folder_path_namedbyvideo)
            if platform == 'win':
                folder_path_namedbyvideo += '\\%7d.png'
            elif platform == 'linux':
                folder_path_namedbyvideo += '/%7d.png'
            else:
                print('wrong platform!')
            if decode_type == '709':
                bash_command = f'ffmpeg -i {video_path} -filter_complex "scale=in_color_matrix=bt709" {folder_path_namedbyvideo}'
            elif decode_type == '2020':
                bash_command = f'ffmpeg -i {video_path} -filter_complex "scale=in_color_matrix=bt2020" {folder_path_namedbyvideo}'
            else:
                print(f'!-------wrong decode_type---------!')

            os.system(bash_command)
            print("Hello world")
        else:
            print(f'check the video format! : {item}')

def merges_frame_video_ffmpeg(img_root, save_root, framerate, start_number=0, encode_type='709', platform ='win'):
    """
    img_root = 
    save_path = 
    merges_frame_video_ffmpeg(, )
    merge VideoPNGs of seperate folders named by original filename into videos.
    -----------------------------------------------------------------------------------------------
    img_root: folder which contains multiple folders of video-frame-imgs 
    save_root: which folder to save the merged videos
    -----------------------------------------------------------------------------------------------
    ---img_root
        ---<video1-frame-imgs>
        ---<video2-frame-imgs>
        ...
    ---save_root
        ---video1-frame-imgs.mp4
        ---video2-frame-imgs.mp4
        ...
    """
    if not os.path.exists(save_root):os.makedirs(save_root)

    for img_folder in os.listdir(img_root):
        img_folder_path = os.path.join(img_root, img_folder)
        if os.path.isdir(img_folder_path) and os.listdir(img_folder_path): # when this is a folder and not empty
            save_path = os.path.join(save_root, img_folder+'.mp4')

            if encode_type == '709':
                bash_command =  f'ffmpeg -r {framerate} -start_number {start_number} -i {img_folder_path}/%4d.png -vcodec libx264 -vf "scale=in_color_matrix=bt709"  -v warning -crf 10 -color_range 1 -colorspace bt709 -color_primaries bt709 -color_trc bt709 {save_path}'
            elif encode_type == '2020':
                # bash_command = f'ffmpeg -r {framerate} -i {img_folder_path} -vcodec  libx264 -vf "scale=in_color_matrix=bt2020"  -v warning -crf 0 -color_range 1 -colorspace bt2020nc -color_primaries bt2020 -color_trc arib-std-b67  {save_path}'
                bash_command = f'ffmpeg -r {framerate} -start_number {start_number} -i {img_folder_path} -vf "scale=in_color_matrix=bt2020:out_color_matrix=bt2020:in_range=limited:out_range=limited" -c:v libx264 -x264-params colorprim=bt2020:transfer=arib-std-b67:colormatrix=bt2020nc -crf 0 -pix_fmt yuv422p10le {save_path}'
            else:
                print(f'!-------wrong encode_type---------!')

            os.system(bash_command)
            # print("Hello world")
        else:
            print(f'"{img_folder_path}" is not the img_folder!')


def random_cut(cut_number, save_path, file_path):
    '''
    cut_number: the number of cutted videos
    save_path: where to save the cutted videos
    file_path: ORG video path
    total_time = 02:00:00 --> specified for the journey video
    '''
    if not os.path.exists(save_path):os.makedirs(save_path)

    for i in range(cut_number):
        time = random.randint(0,0)
        minute = random.randint(0,8)
        if minute == 8:
            second = random.randint(0,51) #!TODO attention
        else:
            second = random.randint(0,54) #!TODO attention
        t = '0' + str(time)
        # m, s, s_end = str(minute), str(second), str(second + 1)
        # bash_command = f'ffmpeg -ss {t}:{m}:{s}.000 -to {t}:{m}:{s_end}.000 -i "{file_path}" -c:v copy -c:a copy "{save_path}journey_{str(i)}.mxf"'
        m, s, s_end = str(minute), str(second), str(second+5)
        bash_command = f'ffmpeg -ss {t}:{m}:{s}.500 -to {t}:{m}:{s_end}.500 -i "{file_path}" -c:v copy -c:a copy "{save_path}\jingbian_{str(i+9)}.mxf"'

        os.system(bash_command)


if __name__=='__main__':
    # video_root = f'C:\\Users\\liumm\\Videos\\max-delta-video\\'
    # save_root = f'C:\\Users\\liumm\\Videos\\max-delta-video-img\\'
    # dump_video_frame_folder_ffmpeg(video_root, save_root, decode_type='2020')

    # img_root = f'C:\\Users\\liumm\\Videos\\SZ-video-img-sdr-v2\\'
    # save_root = f'C:\\Users\\liumm\\Videos\\SZ-video-sdr-v2\\'
    # merges_frame_video_ffmpeg(img_root=img_root, save_root=save_root, framerate=50, encode_type='709',platform ='win')

    img_root = f'C:\\Users\\liumm\\Videos\\hgl\\'
    save_root = f'C:\\Users\\liumm\\Videos\\hgl\\'
    merges_frame_video_ffmpeg(img_root=img_root, save_root=save_root, framerate=25, encode_type='2020',platform ='win')

    # cut_number = 6
    # save_path = r'C:\Users\liumm\Videos\jingbian'
    # file_path=r'C:\Users\liumm\Videos\aaavideo\ColorGamut007-4K-BT2020-HLG-JingbianXAVC.mxf'
    # random_cut(cut_number, save_path, file_path)