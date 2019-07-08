#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 00:06:12 2019

@author: zhiyu
"""
"""
The aims of this program are to crop the RGB and the mask images of the YCB
objects dataset from 1024*1280 to 960*1280, and then resize them to 480*640, so
as not to changing the aspect ratio. Because the objects in the YCB Set are all
in the centers of the images, the crop operation will not make the objects be
cut. And the low resolution may close to the images captured by the commodity
RGB-D cameras.
"""

import os
import cv2
import time
from PIL import Image
from PIL import ImageOps

input_dir = '/mnt/disk/zhiyu/ycb_objects'
output_dir = '/mnt/disk/zhiyu/ycb_preprocessed'

files = os.listdir(input_dir)
for file in files:
    object_file = input_dir + '/' + file
    if os.path.isdir(object_file):
        start_time  = time.time()
        
        print("Start processing", file)
        
        #process the mask images
        masks_dir = object_file + '/masks'
        masks_images = os.listdir(masks_dir)
        for img_name in masks_images:
            img = Image.open(masks_dir + '/' + img_name)
            img = ImageOps.crop(img, (0, 32, 0, 32))
            img.thumbnail((640,480), Image.ANTIALIAS)
            output_name = output_dir + '/' + file + '/masks'
            if not os.path.exists(output_name):
                os.makedirs(output_name)
            img.save(output_name + '/' + img_name)
        
        #process the rgb images
        subfiles = os.listdir(object_file)
        for subfile in subfiles:
            if subfile[-3:] == 'jpg':
                img = cv2.imread(object_file + '/' + subfile)
                img = img[32:992,:,:]
                img = cv2.resize(img, (640, 480))
                output_name = output_dir + '/' + file + '/rgb'
                if not os.path.exists(output_name):
                    os.makedirs(output_name)
                cv2.imwrite(output_name + '/' + subfile, img)
        print("Processing", file, "finished.", "Time used:", time.time()-start_time)

print("All preprocessing finished!")