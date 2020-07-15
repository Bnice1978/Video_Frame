# Usage
# python video_frame.py --input video/pedestrians.mp4 --output images/ --seconds 1
#
# Bart den Nijs, with help from stackoverflow and PyImageSearch
# 14/07/2020

import sys
import argparse
import numpy as np

import cv2
print(cv2.__version__)

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", help="path to video")
ap.add_argument("-o", "--output", help="path to images")
ap.add_argument("-s", "--seconds", type=int, default=1, help="take frame every x seconds")
args = vars(ap.parse_args())

# extract the frames from the video
count = 0
vidcap = cv2.VideoCapture(args["input"])
success,image = vidcap.read()
success = True
while success:
    vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))
    success,image = vidcap.read()
        
    ## Stop when last frame is identified
    image_last = cv2.imread("frame{}.jpg".format(count-1))
    if np.array_equal(image,image_last):
        break
        
    print ('Read frame %d:' % count, success)
    cv2.imwrite( args["output"] + "\\frame%d.jpg" % count, image)
    count += args["seconds"]