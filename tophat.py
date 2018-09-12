import cv2 as cv
import numpy as np

def tophat_demo(image):
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(115,115))
    dst=cv.morphologyEx(gray,cv.MORPH_BLACKHAT,kernel)
    cimage=np.array(gray.shape,np.uint8)
    cimage=100
    cv.add(dst,cv.MORPH_TOPHAT,kernel)
    cv.imshow('tophat',dst)

def hat_binary_demo(image):
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)

    kernel=cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    dst=cv.morphologyEx(gray,cv.MORPH_GRADIENT,kernel)

    cv.imshow('tophat',dst)



src1 = cv.imread('D:/laoluo.jpg', cv.IMREAD_COLOR)  # 读入彩色图片

print(src1.shape)

cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow('image1', src1)
hat_binary_demo(src1)
k = cv.waitKey(0)