import cv2
writer=cv.VideoWriter(output_path,
                          cv.VideoWriter_fourcc(*'mp4v'),
                          30,
                          (round(cap.get(cv.CAP_PROP_FRAME_WIDTH)), round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))))
cap=cv2.VideoCapture('origin_cam6.mp4')
count=0
while(True) :
    is_read,show=cap.read()
    count+=1
    if count < 300 :
        continue
    writer
    
