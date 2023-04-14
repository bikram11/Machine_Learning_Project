from subprocess import call
call(["python","yolov5/featuextractor.py", "--weights", "yolov5s.pt", "--save-txt", "--save-conf", "--conf","0.25", "--features", "features_checked/test", "--source", "raw_data/test/camera_images","--device","0"])
# call(["python","yolov5/feature_extractor.py", "--weights", "yolov5s.pt", "--save-txt", "--temp-feature-dir", "features_checked", "--source", "test/camera_images","--device","cpu"])
# !python detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source data/images