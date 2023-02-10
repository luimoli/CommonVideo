import os, sys


def pulldown(video_root):
    for i in range(6,11,1):
        video_path = os.path.join(video_root, f'test_{i}.mov')
        save_video_path = os.path.join(video_root, f'test_{i}_pd.mov')

        command = f'ffmpeg -i {video_path} \
            -vf "fieldmatch,yadif,decimate" \
            -c:v prores_ks \
            -profile:v 3 \
            -vendor apl0 \
            -bits_per_mb 8000 \
            -pix_fmt yuv422p10le \
            {save_video_path}'
        os.system(command)

if __name__ == '__main__':
    video_root = "/home/mengmengliu/datasets/Tests/original_LQ_video/"
    pulldown(video_root)