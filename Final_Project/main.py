# -*- coding: UTF-8 -*-
import cv2 as cv
import argparse
import numpy as np
import time
from utils import choose_run_mode, load_pretrain_model, set_video_writer
from Pose.pose_visualizer import TfPoseVisualizer
from Action.recognizer import load_action_premodel, framewise_recognize,get_pose_dict
from Action.classifier import  classify,draw_box,suspicious_delay
import glob
import sys
# 导入相关模型
#estimator = load_pretrain_model('VGG_origin')
estimator = load_pretrain_model('mobilenet_thin')
action_classifier = load_action_premodel('Action/framewise_recognition_under_scene.h5')#action classifier model

# 参数初始化
video_list=[]
video_len=0
realtime_fps = '0.0000'
start_time = time.time()
fps_interval = 1
fps_count = 0
run_timer = 0
frame_count = 0
cam_video=1#cam_video=0->camera  cam_video=1->video
file_p="camera_record/*.mp4"#要读取的视频所在文件夹的路径
is_save=False
vid_index=0
#读取视频列表
if(cam_video==1):
    video_list=glob.glob(file_p)
    video_len=len(video_list)
    print(video_list)
    if(video_len<=0):
        print('No video in that file')
        sys.exit(1)
cap = choose_run_mode(cam_video,video_list,vid_index)#读取视频
#video_writer = set_video_writer(cap, write_fps=int(7.0))
video_writer = set_video_writer(cap, write_fps=int(30.0),output_path='after_cam.mp4')
video_writer_origin=set_video_writer(cap, write_fps=int(30.0),output_path='origin_cam.mp4')
vid_index+=1

if is_save:
    f = open('origin_data.txt', 'a+')
cur_pose={}
befo_pose={}
cur_box={}
cur_tag={}
delay_rec={}
detect_thresh=5
is_suspicious=False
ROI=[518,564,789,717] #敏感区域
#ROI=[1,1,2,2]
sus_thresh=5 #逗留检测阈值
while cv.waitKey(1) < 0:
    has_frame, show = cap.read()
    if has_frame:
        video_writer_origin.write(show)
        fps_count += 1
        frame_count += 1
        # pose estimation
        humans = estimator.inference(show)
        # get pose info
        pose = TfPoseVisualizer.draw_pose_rgb(show, humans)  # return frame, joints, bboxes, xcenter 
        #返回npimg(检测结果图), joints(每一帧所有的关节点，原图尺寸下的坐标), bboxes(框出人的ROI),
        # xcenter(每个人的同一个关节点坐标,用以区分开每个人对应的bboxes), record_joints_norm(720p下的相对二维坐标,即绝对坐标除以尺寸)
       #每5帧更新一次pose,帧都更新一次box
        get_pose_dict(pose,cur_pose,frame_count,cur_box)
        if(frame_count%5==0):
            classify(befo_pose,cur_pose,frame_count,cur_tag)#动作分类
            suspicious_delay(ROI,delay_rec,cur_box,cur_tag,cur_pose,sus_thresh)
        show=draw_box(show,cur_tag,cur_box,frame_count)#画出结果
        height, width = show.shape[:2]
        # 显示实时FPS值
        if (time.time() - start_time) > fps_interval:
            # 计算这个interval过程中的帧数，若interval为1秒，则为FPS
            realtime_fps = fps_count / (time.time() - start_time)
            fps_count = 0  # 帧数清零
            start_time = time.time()
        fps_label = 'FPS:{0:.2f}'.format(realtime_fps)
        cv.putText(show, fps_label, (width-160, 25), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        # 显示检测到的人数
        num_label = "Human: {0}".format(len(humans))
        cv.putText(show, num_label, (5, height-45), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        # 显示目前的运行时长及总帧数
        if frame_count == 1:
            run_timer = time.time()
        run_time = time.time() - run_timer
        time_frame_label = '[Time:{0:.2f} | Frame:{1}]'.format(run_time, frame_count)
        cv.putText(show, time_frame_label, (5, height-15), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        cv.imshow('Action Recognition based on OpenPose', show)
        video_writer.write(show)
        if is_save:
            joints_norm_per_frame = np.array(pose[-1]).astype(np.str)
            f.write(' '.join(joints_norm_per_frame))
            f.write('\n')
    elif(cam_video==1 and vid_index<video_len):
        cap.release()
        video_writer.release()
        video_writer_origin.release()
        cap=choose_run_mode(cam_video,video_list,vid_index)
        video_writer = set_video_writer(cap, write_fps=int(30.0),output_path='after_cam.mp4')
        video_writer_origin= set_video_writer(cap, write_fps=int(30.0),output_path='origin_cam.mp4')
        vid_index+=1
        # 采集数据，用于训练过程(for training)
    else:
        break
video_writer.release()
video_writer_origin.release()
cap.release()
if is_save:
    f.close()

