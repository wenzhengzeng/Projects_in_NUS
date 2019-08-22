import cv2 as cv
import numpy as np
img=cv.imread("C:/Users/Alex/img/img/nus_p.png",1)
print(img.shape)
kernel1=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
kernel2=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
r1=cv.filter2D(img,-1,kernel1)
r2=cv.filter2D(img,-1,kernel2)
cv.imshow("original",img)
cv.imshow("r1",r1)
cv2.imwrite(path1+'9.jpg',r1)
cv.imshow("r2",r2)
cv2.imwrite(path1+'10.jpg',r2)
'''cv.imwrite("C:/Users/Alex/img/img/321.png",r)'''
cv.waitKey(0)
