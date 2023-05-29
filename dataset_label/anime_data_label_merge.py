import numpy as np
import json

label1 = r'dataset_label/AnimeEdge_V1_label/clip_label_MOVIE.json'
label2 = r'dataset_label/AnimeEdge_V1_label/clip_label_TV.json'

with open(label1, 'r') as f:
        content1 = json.load(f)
        
with open(label2, 'r') as f:
        content2 = json.load(f)

new = {**content1, **content2}

label_save_path = r'./clip_label_v1.json'
with open(label_save_path,"w",encoding="utf-8") as f:
        json.dump(new, f)


# verify
with open(label_save_path, 'r') as f:
        total_label = json.load(f)
        print(len(total_label))
        print(total_label['0000'])