import os
import cv2
from tqdm import tqdm
basepath = 'BDDA/validation'
entries = os.listdir(basepath)
entries.sort()

camera_image_path = 'raw_data/validation/camera_images'
gazemap_path = 'raw_data/validation/gazemap_images'

if not os.path.exists(gazemap_path):
    os.makedirs(gazemap_path)


if not os.path.exists(camera_image_path):
    os.makedirs(camera_image_path)

for each_folder in entries:
    if "videos" in each_folder:
        print(each_folder)
        source_prefix = each_folder.split('_')
        inner_entries = os.listdir(basepath+"/"+each_folder)
        inner_entries.sort()
        for inner_files in tqdm(inner_entries):
            # print(inner_files)
            videocap = cv2.VideoCapture(basepath+"/"+each_folder+"/"+inner_files)
            
            count = 0
            while(True) and count < 10:
                ret, frame = videocap.read()
                if ret:
                    if(source_prefix[0]=="gazemap"):
                        cv2.imwrite(gazemap_path+'/%d_%d.jpg'%(int(inner_files[:-12]),count),frame)
                    else:
                        cv2.imwrite(camera_image_path+'/%d_%d.jpg'%(int(inner_files[:-4]),count),frame)
                    count +=1
                else:
                    break
            
            videocap.release()

     
            





