import cvlib
import cv2
import math
import numpy


def cvimg_to_list2(img):
    out_list = list()
    height, width = img.shape[0], img.shape[1]

    for y in range(height):
        for x in range(width):
            out_list.append(tuple(img[y,x]))
    
    return out_list




def unsharp_mask(n):
    s = 4.5
    start_index = -n//2
    mask_kernel = [[calc(start_index+x,start_index + y,s) if (start_index+x,start_index+y) != (0,0) else 1.5 for x in range(n)] for y in range(n)]
    
    return mask_kernel

def calc(x,y,s):
    retVal = - ( 1 / (2*math.pi*s**2)) * math.e ** (- (x**2 + y**2)/(2*s**2))
    return retVal


img = cv2.imread('image.png')
kernel = numpy.array(unsharp_mask(11))
filtered_img = cv2.filter2D(img, -1, kernel)    
cv2.imshow("filtered", filtered_img)
cv2.waitKey(0)
