import os

from pathlib import Path

def video_encode(img_root, save_root, framerate, start_number=0, encode_type='709'):
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
    os.makedirs(save_root, exist_ok=True)
    img_root = Path(img_root)
    save_root = Path(save_root)
    folders = [f for f in img_root.iterdir() if f.is_dir()]
    folders = sorted(folders)
    for folder in folders:
        if '016' not in str(folder) and '017' not in str(folder): #TODO # exclude unwanted videos
        # if True:
            if any(folder.glob('*')):
                save_path = save_root / (folder.name + '.mp4')
                if not save_path.exists(): # only encode those not encoded
                    if encode_type == '709':
                        # bash_command =  f'ffmpeg -r {framerate} -start_number {start_number} -i {img_folder_path}/%5d.png -vcodec libx264 -vf "scale=in_color_matrix=bt709"  -v warning -crf 10 -color_range 1 -colorspace bt709 -color_primaries bt709 -color_trc bt709 {save_path}'
                        bash_command = f'ffmpeg -r {framerate} -start_number {start_number} -i {folder}/%5d.png -c:v libx264 -b:v 20000k -pix_fmt yuv420p -color_range tv -colorspace bt709 -color_primaries bt709 -color_trc bt709 -vf "scale=in_color_matrix=bt709:out_color_matrix=bt709:in_range=pc:out_range=tv" {save_path}'
                    elif encode_type == '2020':
                        # bash_command = f'ffmpeg -r {framerate} -i {img_folder_path} -vcodec  libx264 -vf "scale=in_color_matrix=bt2020"  -v warning -crf 0 -color_range 1 -colorspace bt2020nc -color_primaries bt2020 -color_trc arib-std-b67  {save_path}'
                        bash_command = f'ffmpeg -r {framerate} -start_number {start_number} -i {folder} -vf "scale=in_color_matrix=bt2020:out_color_matrix=bt2020:in_range=limited:out_range=limited" -c:v libx264 -x264-params colorprim=bt2020:transfer=arib-std-b67:colormatrix=bt2020nc -crf 0 -pix_fmt yuv422p10le {save_path}'
                    else:
                        print(f'!-------wrong encode_type---------!')
                    os.system(bash_command)
            else:
                print(folder, '---!empty!')
            

        


    # for img_folder in os.listdir(img_root):
    #     img_folder_path = os.path.join(img_root, img_folder)
    #     if os.path.isdir(img_folder_path) and os.listdir(img_folder_path): # when this is a folder and not empty
    #         save_path = os.path.join(save_root, img_folder+'.mp4')
    #         if not os.path.exists(save_path):
    #             if encode_type == '709':
    #                 # bash_command =  f'ffmpeg -r {framerate} -start_number {start_number} -i {img_folder_path}/%5d.png -vcodec libx264 -vf "scale=in_color_matrix=bt709"  -v warning -crf 10 -color_range 1 -colorspace bt709 -color_primaries bt709 -color_trc bt709 {save_path}'
    #                 bash_command = f'ffmpeg -r {framerate} -start_number {start_number} -i {img_folder_path}/%5d.png -c:v libx264 -b:v 10000k -color_range tv -colorspace bt709 -color_primaries bt709 -color_trc bt709 -vf "scale=in_color_matrix=bt709:out_color_matrix=bt709:in_range=pc:out_range=tv" {save_path}'
    #             elif encode_type == '2020':
    #                 # bash_command = f'ffmpeg -r {framerate} -i {img_folder_path} -vcodec  libx264 -vf "scale=in_color_matrix=bt2020"  -v warning -crf 0 -color_range 1 -colorspace bt2020nc -color_primaries bt2020 -color_trc arib-std-b67  {save_path}'
    #                 bash_command = f'ffmpeg -r {framerate} -start_number {start_number} -i {img_folder_path} -vf "scale=in_color_matrix=bt2020:out_color_matrix=bt2020:in_range=limited:out_range=limited" -c:v libx264 -x264-params colorprim=bt2020:transfer=arib-std-b67:colormatrix=bt2020nc -crf 0 -pix_fmt yuv422p10le {save_path}'
    #             else:
    #                 print(f'!-------wrong encode_type---------!')

    #             os.system(bash_command)

    #     else:
    #         print(f'"{img_folder_path}" is not the img_folder!')


if __name__ == '__main__':
    frames_folder_root = Path("/dataset2/oldanime_smore/results/step3_gan_3LBOs_datasetV1_net_g_40000/cmp_images_old/")
    save_video_root = frames_folder_root.parent / "cmp_videos_old_test"
    # video_encode(frames_folder_root, save_video_root, 23.976)
    video_encode(frames_folder_root, save_video_root, 29.97)