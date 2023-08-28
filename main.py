from video_decode import decode_videos_as_folder

if __name__ =='__main__':
    file_root = r"/dataset2/oldfilm_smore/clips_deinterlaced/part2/"
    save_root = r"/dataset2/oldfilm_smore/images_deinterlaced/"
    decode_videos_as_folder(file_root, save_root)