import cv2
import numpy as np
import os
from hoggy import HoG

def load_img(dir_name,img_list):#考虑添加对图像的预处理,以避免噪声影响
    for file_name in os.listdir(r"./"+dir_name):
        img=cv2.imread(dir_name+"/"+file_name)
        if(img.shape[2]!=3):
            print('required 3 channel image')
            break
        img_list.append(img)
    return 

def get_HoG(img_list,HoG_list):#这里直接将图像尺寸转换成64*128，或许可以参考网上从原图截取一个64*128的rect
    stan_shape=(64,128,3)
    
    for i in range(len(img_list)):
        if(img_list[i].shape != stan_shape):
            img_list[i]=cv2.resize(img_list[i],stan_shape[:2],interpolation=cv2.INTER_AREA)
        gray=cv2.cvtColor(img_list[i],cv2.COLOR_BGR2GRAY)
        HoG_list.append(HoG(gray))
    '''
    hog=cv2.HOGDescriptor()
    for i in range(len(img_list)):
        if(img_list[i].shape != stan_shape):
            img_list[i]=cv2.resize(img_list[i],stan_shape[:2],interpolation=cv2.INTER_AREA)
        gray=cv2.cvtColor(img_list[i],cv2.COLOR_BGR2GRAY)
        HoG_list.append(hog.compute(gray))
        tmp=hog.compute(gray)
        print(type(tmp))
        print(type(tmp[0]))
        print(type(tmp[2][0]))
        '''
    return
    
