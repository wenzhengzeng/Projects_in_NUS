import imgaug as ia
from imgaug import augmenters as iaa
import cv2
from tools import load_img

def create_img_data(input_file,output_file):
    #seq=iaa.Sequential([iaa.Fliplr(0.5),iaa.GaussianBlur(sigma=(0,3.0))])
    seq=iaa.SomeOf((1,4),[iaa.Fliplr(0.5),iaa.Flipud(1.0),iaa.GaussianBlur(1.0),iaa.AdditiveGaussianNoise()])
    img_list=[]
    load_img(input_file,img_list)
    load_img(input_file,img_list)
    img_aug=seq.augment_images(img_list)
    for i in range(len(img_aug)):
        cv2.imwrite(output_file+'/i_imgaug_'+str(i)+'.jpg',img_aug[i])
    


input_file='train_data/original_train/p'
output_file='train_data/train/p'
create_img_data(input_file,output_file)