import cv2
import numpy as np
import os
from sys import argv

TARGET_SIZE = 384

def resize(img):
    r,c,d = img.shape

    if r<c:
        padded_img = np.zeros((c,c,d))
        padded_img[(c-r)/2:(c-r)/2+r, :, :] = img
    else:
        padded_img = np.zeros((r,r,d))
        padded_img[:,(r-c)/2:(r-c)/2+c,:]

    # cv2.imwrite('padded_img.jpg',padded_img)

    resized_img = cv2.resize(padded_img, (TARGET_SIZE, TARGET_SIZE))

    return resized_img

def scale_images(dir):
    output_dir = dir+'_scaled/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for file in os.listdir(dir):
        img = cv2.imread(dir+'/'+file)
        img_mod = resize(img)
        cv2.imwrite(output_dir+file,img_mod)

if len(argv) < 2:
    print 'Enter the name of the folder containing the images as a command line argument'
    exit(0)
else:
    input_dir = argv[1]
    if input_dir[-1] == '/':
        input_dir = input_dir[:-1]
scale_images(input_dir)
