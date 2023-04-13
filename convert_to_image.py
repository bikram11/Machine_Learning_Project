import os
import cv2

basepath = './BDDA/test'
entries = os.listdir(basepath)
entries.sort()

camera_image_path = 'test/camera_images'
gazemap_path = 'test/gazemap_images'

if not os.path.exists(gazemap_path):
    os.makedirs(gazemap_path)


if not os.path.exists(camera_image_path):
    os.makedirs(camera_image_path)

for each_folder in entries:
    if "gazemap" in each_folder:
        inner_entries = os.listdir(basepath+"/"+each_folder)
        inner_entries.sort()
        for inner_files in inner_entries:
            videocap = cv2.VideoCapture(basepath+"/"+each_folder+"/"+inner_files)
            
            count = 0
            while(True and count<10):
                ret, frame = videocap.read()
                if ret:
                    cv2.imwrite(gazemap_path+'/%d_pure_hm_%d.jpg'%(int(inner_files[:-12]),count),frame)
                    count +=1
                else:
                    break
            
            videocap.release()

    if "camera" in each_folder:
        inner_entries = os.listdir(basepath+"/"+each_folder)
        inner_entries.sort()
        for inner_files in inner_entries:
            videocap = cv2.VideoCapture(basepath+"/"+each_folder+"/"+inner_files)
            
            count = 0
            while(True and count<10):
                ret, frame = videocap.read()
                if ret:
                    cv2.imwrite(camera_image_path+'/%d_%d.jpg'%(int(inner_files[:-4]),count),frame)
                    count +=1
                else:
                    break
            
            videocap.release()
     
            





