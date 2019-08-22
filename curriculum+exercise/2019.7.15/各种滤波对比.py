import cv2
import numpy as np
import time

path="C:/Users/Alex/img/img/nus_p.png"
path1='C:/Users/Alex/Desktop/'
img=cv2.imread(path,1)

#img = cv2.resize(img,(1920,1080))

cv2.imshow("original picture",img)
cv2.imwrite(path1+'0.jpg',img)
bilatera0=cv2.bilateralFilter(img,7,400,400)#7 20 20 are sigma color value and sigma space value affects cordinates space and color space 
cv2.imshow("bilateral0",bilatera0)
cv2.imwrite(path1+'1.jpg',bilatera0)
img0=bilatera0

bilateral=cv2.bilateralFilter(img,7,200,200)#7 20 20 are sigma color value and sigma space value affects cordinates space and color space 
cv2.imshow("bilateral",bilateral)
cv2.imwrite(path1+'2.jpg',bilateral)
img1=bilateral

gaussian=cv2.GaussianBlur(img,(9,9),0)
cv2.imshow("GaussianBlur",gaussian)
cv2.imwrite(path1+'3.jpg',gaussian)
blured=gaussian

gaussian1=cv2.GaussianBlur(bilateral,(3,3),0)
cv2.imshow("GaussianBlur1",gaussian1)
cv2.imwrite(path1+'4.jpg',gaussian1)
blured1=gaussian1

canny=cv2.Canny(gaussian1,20,180)#This demand two thresholds from us i.e; 20 and 170 this is like lower and upper value 
cv2.imshow("canny0",canny)
cv2.imwrite(path1+'5.jpg',canny)

canny1=cv2.Canny(bilateral,20,180)#This demand two thresholds from us i.e; 20 and 170 this is like lower and upper value 
cv2.imshow("canny1",canny1)
cv2.imwrite(path1+'6.jpg',canny1)


   
cv2.waitKey(0)
cv2.destroyAllWindows() 
