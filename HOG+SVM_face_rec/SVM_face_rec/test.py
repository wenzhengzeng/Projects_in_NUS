import cv2
import numpy as np
from tools import load_img,get_HoG
from sklearn import metrics


def validate(dir_name):
    img_list=[]
    HoG_list=[]
    labels=[]
    #load positive validation samples
    load_img(dir_name+'/p',img_list)
    for i in range(len(img_list)):
        labels.append(1)
    #load negtive validation samples
    tmp=len(img_list)
    load_img(dir_name+'/n',img_list)
    for i in range(len(img_list)-tmp):
        labels.append(-1)
    #get HoG features
    HoG_list=[]
    get_HoG(img_list, HoG_list)
    #SVM
    svm=cv2.ml.SVM_load('first_train.xml')
    _,pred=svm.predict(np.array(HoG_list))
    pred=[int(i) for i in pred]
    print("on validation set,the accuracy is ",metrics.accuracy_score(labels,pred))


'''
def evaluate(dir_name)
'''   

#validate('train_data/validation')
validate('train_data/test')