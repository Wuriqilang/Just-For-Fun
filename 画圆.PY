import cv2
import numpy as np
from tkinter import *
'''
for i in range(0,25):
    radius = np.random.randint(5,high = 200)#生成1个[5,200)的随机数
    color = np.random.randint(0,high = 256,size = (3,)).tolist()#生成3个[0,256)的随机数
    pt = np.random.randint(0,high = 300,size = (2,))#生成2个[0,300)的随机数
'''
#cv2.circle(Canvas,tuple(pt),radius[i],color[i],-1)#画圆
cv2.circle(Canvas,(0,0),2,(255,255,255),-1)
cv2.imshow("Canvas",Canvas)
cv2.waitKey(0)