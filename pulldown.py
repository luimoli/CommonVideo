import os, sys
from pathlib import Path

def pulldown(video_root, save_root, save_suffix=''):
    """_summary_

    Args:
        video_root (_type_): _description_
        save_root (_type_): _description_
        save_suffix (str, optional): Defaults to '', this will result exactly same file name
                                     e.g. '_pd', results will add '_pd' at the end of the file name.
    """
    os.makedirs(save_root, exist_ok=True)
    root = Path(video_root)
    sroot = Path(save_root)
    files = [f for f in root.iterdir() if f.is_file()]
    for file_path in files:
        if save_suffix:
            # save_path = sroot.joinpath(file_path.stem + save_suffix,  file_path.suffix)
            save_path = sroot / (file_path.stem + save_suffix + file_path.suffix)
        else:
            save_path = sroot / file_path.name
        print(save_path)
        command = f'ffmpeg -i {file_path} \
            -vf "fieldmatch,yadif,decimate" \
            -c:v prores_ks \
            -profile:v 3 \
            -vendor apl0 \
            -bits_per_mb 8000 \
            -pix_fmt yuv422p10le \
            {save_path}'
        os.system(command)


if __name__ == '__main__':
    video_root = "/dataset2/oldanime_smore/clips/pulldown/"
    save_root = "/dataset2/oldanime_smore/clips/pulldown_badcase/"
    pulldown(video_root,save_root,'_pulldown')