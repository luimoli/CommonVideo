from glob import glob
import os
import random

def concat_videos(files_root, save_path):
    """_summary_
    Args:
        files_root (str): contain videos
        save_path (str): result video's path.
    """
    all_paths = glob(f'{files_root}/*')
    all_paths = sorted(all_paths)
    print(f'total {len(all_paths)} videos!')
    concat_file_list = []
    for path in all_paths:
        if os.path.isfile(path):
            file_name = os.path.basename(path)[:-4]
            print(file_name)
            concat_file_list.append(path)
    with open('./mylist.txt','w') as f:
	    for i in concat_file_list:
                f.write(f'file \'{i}\'' + '\n')

    save_folder = os.path.dirname(save_path)
    if not os.path.exists(save_folder): os.makedirs(save_folder)


    bash_command = f'ffmpeg -f concat -safe 0 -i "mylist.txt" -c copy "{save_path}"'
    os.system(bash_command)

if __name__ == '__main__':


    file_root = '/home/mengmengliu/datasets/Tests/original_LQ_video/macross_edge_clips/'
    save_path = '/home/mengmengliu/datasets/Tests/original_LQ_video/macross.mov'
    concat_videos(file_root, save_path)
    # ffmpeg -f concat -safe 0 -i "mylist.txt" -c copy "/home/mengmengliu/datasets/Tests/original_LQ_video/macross.mov"