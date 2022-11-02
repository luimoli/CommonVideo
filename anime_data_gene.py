from glob import glob
import os
from pickle import TRUE
import random
from tqdm import tqdm
import math
import json
import subprocess


def get_video_duration(file_path):
    """_summary_
    Args:
        file_path (str): _description_
    Returns:
        list(int): [time, minute, second]
    """
    bash_command = f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 -sexagesimal "{file_path}"'
    res = subprocess.run(bash_command, shell=True, stdout=subprocess.PIPE)
    time = res.stdout # b'0:00:17.017000\r\n'
    timestr = time.decode('utf-8')
    time_list = timestr[:-2].split(':') # remove \r\n and split by ":"
    assert len(time_list) == 3
    time_list = [int(float(time_list[0])), int(float(time_list[1])), int(float(time_list[2]))]
    return time_list 


def generate_random_n_same_seq(range_a, range_b, res_seq_num, auto_num_cal=False):
    """
    [rangea, rangeb]
    Args:
        range_a (int): (in time sequence it is) 0
        range_b (int): limit_m
        seq_num (_type_): _description_
        auto_num_cal: get 80% of [range_a, range_b], in which total num al
    """
    if auto_num_cal:
        seq_num = int(len(range(range_a, range_b+1)) * 0.8)
    else:  
        seq_num = res_seq_num

    total_num = len(range(range_a, range_b+1))

    if seq_num <= total_num: # get less clips than minute seq num
        res_list = random.sample(range(range_a, range_b+1), seq_num)
    else:
        fol = math.floor(seq_num / total_num)
        res_list = []
        for i in range(fol):
            res_list.extend(random.sample(range(range_a, range_b+1), total_num))
        seq_left_num = seq_num - fol*total_num
        res_list.extend(random.sample(range(range_a, range_b+1), seq_left_num))

        # res_list = []
        # for i in range(fol):
        #     res_list.extend(range(range_a, range_b+1))
        # seq_left_num = seq_num - fol*total_num
        # res_list.extend(random.sample(range(range_a, range_b+1), seq_left_num))
      
    assert len(res_list) == seq_num

    return res_list



def random_cut(cut_number, cut_duration, save_path, file_root1, file_root2, label_save_path, auto_number):
    """randomly cut clips of videos and save in specified root and keep the label information.
     TODO when time is not 0.(video is very long)
    Args:
        cut_number (int): _description_
        cut_duration (int): unit(s) the duration of the cutted clip
        save_path (str): save folder path
        file_root1 (str): video folder 1
        file_root2 (str): video folder 2
        label_save_path (str): save the label of the generated dataset
        auto_number (bool): if True, the calculate the <cut_number> according to video duration.(in func[generate_random_n_same_seq])
    """

    if not os.path.exists(save_path):os.makedirs(save_path)
    
    file_paths1 = glob(f'{file_root1}\\*.mp4')
    file_paths2 = glob(f'{file_root2}\\*.mp4')
    file_list = []
    file_list.extend(file_paths1)
    file_list.extend(file_paths2)
    print(file_list)
    print(len(file_list))

    clip_num = 0
    label_dic = {} # save the label

    # for video_path in glob(f'{file_root}\\*.mp4'):
    for video_path in file_paths1:
        limit_t, limit_m, limit_s = get_video_duration(video_path)

        m_seq = generate_random_n_same_seq(0, limit_m, cut_number, auto_num_cal=auto_number)

        # for i in range(cut_number):
        for i in range(len(m_seq)):
            time = random.randint(0,limit_t)
            minute = m_seq[i]
            if minute == limit_m:
                buffer_time = 2 # TODO
                if (limit_s - buffer_time) < cut_duration:
                    minute -= 1  # TODO maybe cut_duration is very large, here we presume that it is within 1 minute.
                    second = 59 - (cut_duration - limit_s + buffer_time)
                else:
                    second = random.randint(0, limit_s - buffer_time - cut_duration) 
            else:
                second = random.randint(0,59) 

            t, m, s = str(time).zfill(2), str(minute).zfill(2), str(second).zfill(2)
            cut_duration_str = str(cut_duration).zfill(2)
            save_file_name = str(clip_num).zfill(3)
            
            bash_command = f'ffmpeg -ss {t}:{m}:{s} -t 00:00:04 -i "{video_path}" -c:v copy -c:a copy -strict -2 "{save_path}\{save_file_name}.mp4"'
            os.system(bash_command)

            label_dic[save_file_name] = {"original_filesource":video_path, "start_timestamp":f'{t}:{m}:{s}'}
            
            clip_num += 1
    

    for video_path in file_paths2:
        limit_t, limit_m, limit_s = get_video_duration(video_path)

        m_seq = generate_random_n_same_seq(0, limit_m, cut_number, auto_num_cal=auto_number)

        # for i in range(cut_number):
        for i in range(len(m_seq)):
            time = random.randint(0,limit_t)
            minute = m_seq[i]
            if minute == limit_m:
                buffer_time = 2 # TODO
                if (limit_s - buffer_time) < cut_duration:
                    minute -= 1  # TODO maybe cut_duration is very large, here we presume that it is within 1 minute.
                    second = 59 - (cut_duration - limit_s + buffer_time)
                else:
                    second = random.randint(0, limit_s - buffer_time - cut_duration) 
            else:
                second = random.randint(0,59) 

            t, m, s = str(time).zfill(2), str(minute).zfill(2), str(second).zfill(2)
            cut_duration_str = str(cut_duration).zfill(2)
            save_file_name = str(clip_num).zfill(3)
            
            bash_command = f'ffmpeg -ss {t}:{m}:{s} -t 00:00:04 -i "{video_path}" -c:v copy -c:a copy "{save_path}\{save_file_name}.mp4"'
            os.system(bash_command)

            label_dic[save_file_name] = {"original_filesource":video_path, "start_timestamp":f'{t}:{m}:{s}'}
            
            clip_num += 1


    with open(label_save_path,"w",encoding="utf-8") as f:
        # f.write(json.dumps(label_dic))
        json.dump(label_dic, f)



def mkv_to_mp4(file_root, save_root):
    """_summary_
    Args:
        file_root (str): mkv videos' root
        save_root (str): saved mp4 videos' root
    """
    file_paths = glob(f'{file_root}\\*.mkv')
    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        save_path = os.path.join(save_root, f'{file_name[:-4]}.mp4')
        bash_command = f'ffmpeg -i "{file_path}" -codec copy -strict -2 "{save_path}"'
        # bash_command = f'ffmpeg -i "{file_path}" -vcodec copy -acodec copy -strict -2 "{save_path}"'
        os.system(bash_command)





if __name__ == '__main__':
    # file_path = r"\\192.168.100.201\Media-Dev\Video_Depo\动漫\Hataraku Saibou\[Kamigami][Hataraku Saibou][01][720P][CHS].mp4"

   
    save_path = r"\\192.168.100.201\Media-Dev\Video_Depo\动漫\Anime_Dataset\1080p"
    file_root1 = r'\\192.168.100.201\Media-Dev\Video_Depo\动漫\Fate stay night UBW mp4'
    file_root2 = r"\\192.168.100.201\Media-Dev\Video_Depo\动漫\saoali"
    cut_number = 20
    cut_duration = 4
    label_save_path = r"\\192.168.100.201\Media-Dev\Video_Depo\动漫\Anime_Dataset\label_1080p.json"
    auto_number = True
    # random_cut(cut_number, cut_duration, save_path, file_root1, file_root2, label_save_path, auto_number)

    # with open(label_save_path, 'r') as f:
    #     content = json.load(f)
    #     print(content['400'])
    #     print(len(content))

    # file = r"\\192.168.100.201\Media-Dev\Video_Depo\动漫\Fate stay night UBW\[Kamigami] Fate stay night UBW - 16 [1080p x265 Ma10p FLAC Sub(Eng,Jap)].mkv"
    # save_folder = r"\\192.168.100.201\Media-Dev\Video_Depo\动漫\lmm\720p\nonstop_img"
    # decode(file_path=file,save_folder=save_folder)
    # print(get_video_duration(file))


    # file_root = r'\\192.168.100.201\Media-Dev\Video_Depo\动漫\Fate stay night UBW'
    # save_root = r'\\192.168.100.201\Media-Dev\Video_Depo\动漫\Fate stay night UBW mp4'
    # mkv_to_mp4(file_root, save_root)