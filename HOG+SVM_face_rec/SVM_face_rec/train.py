import cv2
import numpy as np
from tools import load_img,get_HoG
from sklearn import metrics

def validate(svm,dir_name):
    img_list=[]
    HoG_list=[]
    labels=[]
    #load positive validation samples
    dir_name=dir_name+'/validation'
    #dir_name='train_data/validation'
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
    #svm=cv2.ml.SVM_load('first_train.xml')
    _,pred=svm.predict(np.array(HoG_list))
    pred=[int(i) for i in pred]
    cur_acc=metrics.accuracy_score(labels,pred)
    print("on validation set,the current accuracy is ",cur_acc)
    return pred,cur_acc

def train(o_dir_name):
    dir_name=o_dir_name+'/train'
    labels=[]
    img_list=[]
    #get positive img
    load_img(dir_name+'/p',img_list)
    for i in range(len(img_list)):
        labels.append(1)
    #get negtive img
    tmp=len(img_list)
    load_img(dir_name+'/n',img_list)
    for i in range(len(img_list)-tmp):
        labels.append(-1)
    #get HoG feature list
    HoG_list=[]
    get_HoG(img_list, HoG_list)
    #info print
    print('received ',tmp,' positive sample(s)')
    print('received',len(img_list)-tmp,' negtive sample(s)')
    print('start training')
    #train SVM 考虑基于Hard Example对分类器二次训练https://www.xuebuyuan.com/2083806.html
    best_c=0
    best_gamma=0
    best_acc=0
    for C in [0.01,0.1,1,5,10,50,100]:
        for gamma in [0.1,0.5,0.7,1,1.5,2,2.5,5,10]:#,1,1.5,2,5,10]:
            svm=cv2.ml.SVM_create()
            svm.setC(C)
            svm.setGamma(gamma)
            svm.setType(cv2.ml.SVM_C_SVC)
            svm.setKernel(cv2.ml.SVM_LINEAR)
            svm.train(np.array(HoG_list),cv2.ml.ROW_SAMPLE,np.array(labels))
            _,cur_acc=validate(svm,o_dir_name)
            if(cur_acc>best_acc):
                best_c=C
                best_gamma=gamma
                best_acc=cur_acc
    svm=cv2.ml.SVM_create()
    svm.setC(best_c)
    svm.setGamma(best_gamma)
    svm.setType(cv2.ml.SVM_C_SVC)
    svm.setKernel(cv2.ml.SVM_LINEAR)
    svm.train(np.array(HoG_list),cv2.ml.ROW_SAMPLE,np.array(labels))
    svm.save('first_train.xml')
    print('svm data has been saved')




train("train_data")
