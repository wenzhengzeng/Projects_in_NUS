# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 08:34:24 2019

@author: aiss
"""

import cv2
import numpy as np
import math
#import matplotlib.pyplot as plt


class Hog_descriptor():
    def __init__(self, img, cell_size=16, bin_size=8):
        self.img = img
        self.img = np.sqrt(img / np.max(img))
        self.img = img * 255
        self.cell_size = cell_size
        self.bin_size = bin_size
        self.angle_unit = 360 // self.bin_size
        if type(self.bin_size)!=int:
            raise AssertionError("bin_size should be integer,")
        if type(self.cell_size)!=int:
            raise AssertionError("bin_size should be integer,")
        if type(self.angle_unit)!=int:
            raise AssertionError("bin_size should be integer,")

    def extract(self):
        height, width = self.img.shape
        gra_magnitude, gra_angle = self.global_gradient()
        gra_magnitude = abs(gra_magnitude)
        cell_gra_vector1 = [[[0 for i in range(self.bin_size)] for i in range(width // self.cell_size) ] for i in range(height // self.cell_size)]
        cell_gra_vector = np.array(cell_gra_vector1, dtype=np.float64)
        for i in range(int(height / self.cell_size)):
            for j in range(int( width / self.cell_size)):
                cell_magnitude = gra_magnitude[i * self.cell_size:(i + 1) * self.cell_size,
                                 j * self.cell_size:(j + 1) * self.cell_size]
                cell_angle = gra_angle[i * self.cell_size:(i + 1) * self.cell_size,
                             j * self.cell_size:(j + 1) * self.cell_size]
                cell_gra_vector[i][j] = self.cell_gra(cell_magnitude, cell_angle)

        #hog_image = self.render_gradient(np.zeros([height, width]), cell_gra_vector)
        hog_vector = []
        for i in range(cell_gra_vector.shape[0] - 1):
            for j in range(cell_gra_vector.shape[1] - 1):
                block_vector = []
                block_vector.extend(cell_gra_vector[i][j])
                block_vector.extend(cell_gra_vector[i][j + 1])
                block_vector.extend(cell_gra_vector[i + 1][j])
                block_vector.extend(cell_gra_vector[i + 1][j + 1])
                magnitude = math.sqrt(sum(i ** 2 for i in block_vector))
                if magnitude != 0:
                    block_vector = [element / magnitude for element in block_vector]
                hog_vector.append(block_vector)
        return np.array(hog_vector).flatten()

    def global_gradient(self):
        SCALE=1
        DELTA=0
        Sobelx = cv2.Sobel(self.img, cv2.CV_64F, 1, 0, ksize=5, scale=SCALE,delta=DELTA)
        Sobely = cv2.Sobel(self.img, cv2.CV_64F, 0, 1, ksize=5, scale=SCALE,delta=DELTA)
        gra_magnitude = cv2.addWeighted(Sobelx, 0.5, Sobely, 0.5, 0)
        gra_angle = cv2.phase(Sobelx, Sobely, angleInDegrees=True)
        return gra_magnitude, gra_angle

    def cell_gra(self, cell_magnitude, cell_angle):
        orientation_centers = [0] * self.bin_size
        for i in range(0,self.cell_size):
            for j in range(0,self.cell_size):
                gra_strength = cell_magnitude[i][j]
                gra_angle = cell_angle[i][j]
                min_angle = int(gra_angle / self.angle_unit)
                max_angle = (min_angle + 1) % self.bin_size
                mod = gra_angle % self.angle_unit
                orientation_centers[min_angle] += (gra_strength * (1 - (mod / self.angle_unit)))
                orientation_centers[max_angle] += (gra_strength * (mod / self.angle_unit))
        return orientation_centers
    
'''
    def render_gradient(self, image, cell_gra):
        cell_width = self.cell_size / 2
        max_mag = np.array(cell_gra).max()
        for x in range(cell_gra.shape[0]):
            for y in range(cell_gra.shape[1]):
                cell_grad = cell_gra[x][y]
                cell_grad /= max_mag
                angle = 0
                for magnitude in cell_grad:
                    angle_radian = math.radians(angle)
                    x1 = int(x * self.cell_size + magnitude * cell_width * math.cos(angle_radian))
                    y1 = int(y * self.cell_size + magnitude * cell_width * math.sin(angle_radian))
                    x2 = int(x * self.cell_size - magnitude * cell_width * math.cos(angle_radian))
                    y2 = int(y * self.cell_size - magnitude * cell_width * math.sin(angle_radian))
                    cv2.line(image, (y1, x1), (y2, x2), int(255 * math.sqrt(magnitude)))
                    angle += self.angle_unit
        return image
'''
def HoG(img):
    hog = Hog_descriptor(img)
    vec = hog.extract()
    '''
    vector=[]
    for i in vec:
        vector.append([i])
    '''
    vector=np.array(vec)
    vector.dtype='float32'
    return vector
#print (np.array(vector).shape)
#plt.imshow(image, cmap=plt.cm.gray)
#plt.show()
'''
img = cv2.imread('C:/Users/lenovo/Desktop/li1.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (128,128),interpolation=cv2.INTER_AREA)
print(HoG(img))
'''