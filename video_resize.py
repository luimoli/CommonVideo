import numpy as np
import os
from pathlib import Path
import cv2


# root = Path('/dataset2/oldfilm_smore/clips')
# save_root = Path('/dataset2/oldfilm_smore/clips2')
# name_list = ['007_01.mxf','007_02.mxf','009_01.mov', '013_01.mp4', '013_02.mp4']

# for name in name_list:
#     name = Path(name)
#     path = root / name
#     # f_re_cmd = f'ffmpeg -i {path} -vf scale=-1:ih/2 {save_root}/{name.stem}_down{name.suffix}'  
#     copy_cmd = f'cp -r {path} {save_root}'  
#     print(copy_cmd)
#     os.system(copy_cmd)




root = Path('/dataset2/oldfilm_smore/images')
save_root = Path('/dataset2/oldfilm_smore/images2')
# name_list = ['007_01.mxf','007_02.mxf','008_01.mp4','009_01.mov', '013_01.mp4', '013_02.mp4']
name_list = ['017.mp4', '018.mp4', '019.mp4']

for name in name_list:
    name = Path(name)
    folder = root / name.stem
    save_folder = save_root / name.stem
    print(save_folder)
    os.makedirs(save_folder, exist_ok=True)
    files = [f for f in folder.iterdir() if f.is_file()]
    for file in files:
        img = cv2.imread(str(file))
        res = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))
        cv2.imwrite(str(save_folder / file.name), res)
