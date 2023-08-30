import os

from pathlib import Path

def video_encode(img_root, save_root, 
                 framerate, bitrate, 
                 vcodec='libx264', 
                 pix_fmt='yuv420p',
                 start_number=0, 
                 encode_type='709', 
                 save_suffix='mp4'
                 ):
    """merge VideoPNGs of seperate folders named by original filename into videos.

    Args:
        img_root (str): folder which contains multiple folders of video-frame-imgs
        save_root (str): which folder to save the merged videos
        framerate (float): 
        bitrate (str): e.g. 20000k; when using vcodec='prores', bitrate is usually not specified.
        vcodec (str): 'libx264', 'prores'
        start_number (int, optional): start to encode. Defaults to 0.
        encode_type (str, optional): _description_. Defaults to '709'.
        save_suffix (str, optional): 'mp4', 'mov'...
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
        # if '016' not in str(folder) and '017' not in str(folder): #TODO # exclude unwanted videos
        if True:
            if any(folder.glob('*')): # this folder is not empty !!!!
                save_path = save_root / (folder.name + f'.{save_suffix}')
                if not save_path.exists(): # only encode those not encoded !!!!
                    
                    if vcodec == 'libx264':
                        if encode_type == '709':
                            # bash_command =  f'ffmpeg -r {framerate} -start_number {start_number} -i {img_folder_path}/%5d.png -vcodec libx264 -vf "scale=in_color_matrix=bt709"  -v warning -crf 10 -color_range 1 -colorspace bt709 -color_primaries bt709 -color_trc bt709 {save_path}'
                            bash_command = f'ffmpeg -r {framerate} -start_number {start_number} -i {folder}/%5d.png -c:v libx264 -b:v {bitrate} -pix_fmt {pix_fmt} -color_range tv -colorspace bt709 -color_primaries bt709 -color_trc bt709 -vf "scale=in_color_matrix=bt709:out_color_matrix=bt709:in_range=pc:out_range=tv" {save_path}'

                        elif encode_type == '2020':
                            # bash_command = f'ffmpeg -r {framerate} -i {img_folder_path} -vcodec  libx264 -vf "scale=in_color_matrix=bt2020"  -v warning -crf 0 -color_range 1 -colorspace bt2020nc -color_primaries bt2020 -color_trc arib-std-b67  {save_path}'
                            bash_command = f'ffmpeg -r {framerate} -start_number {start_number} -i {folder} -vf "scale=in_color_matrix=bt2020:out_color_matrix=bt2020:in_range=limited:out_range=limited" -c:v libx264 -x264-params colorprim=bt2020:transfer=arib-std-b67:colormatrix=bt2020nc -crf 10 -pix_fmt yuv422p10le {save_path}'
                        else:
                            raise ValueError(f'{encode_type} is not supported!')
                        

                    elif vcodec == 'prores':
                        if encode_type == '709':
                            # prores hq
                            bash_command = f'ffmpeg -r {framerate} -start_number {start_number} -i {folder}/%5d.png -c:v prores_ks -profile:v 3 -qscale:v 10 -pix_fmt yuv422p10le -color_range tv -colorspace bt709 -color_primaries bt709 -color_trc bt709 -vf "scale=in_color_matrix=bt709:out_color_matrix=bt709:in_range=pc:out_range=tv" {save_path}'
                        else:
                            raise ValueError(f'{encode_type} is not supported!')
                    
                    else:
                        raise ValueError(f'{vcodec}: this encode method is not supported!')


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
    # frames_folder_root = Path("/home/mengmengliu/code/AnimeSR-dev/results/step1_gan_BasicOPonly_2_net_g_40000/frames")
    # save_video_root = frames_folder_root.parent / "videos"
    frames_folder_root = Path("/home/mengmengliu/code/AnimeSR-dev/results/step3_gan_3LBOs_datasetV1_net_g_10000/frames")
    save_video_root = frames_folder_root.parent / "videos"
    # video_encode(frames_folder_root, save_video_root, 25)  
    video_encode(frames_folder_root, save_video_root, framerate=23.976, bitrate='50000k', save_suffix='mov')
    # video_encode(frames_folder_root, save_video_root, 29.97)