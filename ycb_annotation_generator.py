#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 01:51:21 2019

@author: zhiyu
"""

"""
This program aims to generate annotations as the format of the COCO dataset
Specifically, using the masks images to generate.
Because all the instances are in the center of the images, so not need to padding
when extract the mask.
Also, because the names of the images are in order which means continuous images
look similar, so the image_ids are randomized.
"""

import os
import cv2
import json
import numpy as np
import matplotlib.pyplot as plt
import time
import random
from tools.mask_annotation_generator import create_sub_mask_annotation
from PIL import Image
import PIL.ImageOps


def generateannotation(kind):
    images = []
    annotations = []
    annotation_id = 0
    width = 640
    height = 480
    iscrowd = 0

    
    for file in files:
        category_dir = input_dir+'/'+file
        if os.path.isdir(category_dir):
            category_id = int(file[:2])
            masks_dir = category_dir + '/masks/' + kind
            masks = os.listdir(masks_dir)
            for mask in masks:
                print("Processing", mask)
                image_id = image_id_index[int(mask[:-4])]
                image_id = int(mask[:-4])
                file_name = mask[:-4] + '.jpg'
                image_item = {'file_name':file_name, 'height':height, 'id':image_id, 'width':width}
                images.append(image_item)
                
                # Write information of each mask in the image
                image = cv2.imread(category_dir + '/masks/' + kind + '/' + mask)
                annotation_id += 1
                annotation_item = create_sub_mask_annotation(image, image_id, category_id, annotation_id, iscrowd)
                annotations.append(annotation_item)
                    
                    
    json_data = {'annotations':annotations, 'categories':categories, 'images':images}
    if not os.path.exists(anno_output_dir):
                os.makedirs(anno_output_dir)
    with open(anno_output_dir + '/instances_' + kind + '.json', 'w') as f:
        json.dump(json_data, f)



input_dir = 'path to/ycb_train_val_splited'
anno_output_dir = 'path to/ycb_annotations'

files = os.listdir(input_dir)

categories = []
for file in files:
    category_dir = input_dir+'/'+file
    if os.path.isdir(category_dir):
        category_id = int(file[:2])
        category_name = file[3:]
        category = {'supercategory': category_name, 'id': category_id, 'name': category_name}
        categories.append(category)

start_num = 0
end_num = 21 * 600 - 1
image_id_index = random.sample([i for i in range(start_num, end_num + 1)], 21 * 600)


generateannotation('train')
generateannotation('val')