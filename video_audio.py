import os

from pathlib import Path

def get_audio(video_path, save_audio_root, save_suffix):
    video_path = Path(video_path)
    save_root = Path(save_audio_root)
    file_name = video_path.stem
    save_audio_path = save_root / (file_name+f'.{save_suffix}')
    bash_command = f'ffmpeg -i {video_path} -vn -c:a copy {save_audio_path}'
    os.system(bash_command)


def merge_video_audio(video_path, audio_path, save_root):
    video_path = Path(video_path)
    audio_path = Path(audio_path)
    save_root = Path(save_root)
    save_path = save_root / f'{video_path.stem}_withAudio{video_path.suffix}'
    # print(save_path)
    bash_command = f'ffmpeg -i {video_path} -i {audio_path} -c:v copy -c:a copy {save_path}'
    os.system(bash_command)


if __name__ == '__main__':
    video_path = Path('/home/mengmengliu/code/AnimeSR-dev/results/step3_gan_3LBOs_datasetV1_net_g_10000/videos/macross_zero_BDR.mov')
    audio_path = '/home/mengmengliu/code/AnimeSR-dev/inputs_old/macross_zero_BDR_1080_2398_original.wav'
    save_root = video_path.parent
    merge_video_audio(video_path, audio_path, save_root)