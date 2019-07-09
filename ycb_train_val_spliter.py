#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 23:27:44 2019

@author: zhiyu
"""
"""
The aim of this program is to split the train (two thirds) and the validation (one third) sets.
"""

import os
import random

input_dir = 'path to/ycb_renamed'
output_dir = 'path to/ycb_train_val_splited'

files = os.listdir(input_dir)
for file in files:
    category_dir = input_dir+'/'+file
    if os.path.isdir(category_dir):
        category_id = int(file[:2])
        
        start_num = (category_id - 1) * 600
        end_num = 599 + start_num
        index = random.sample([i for i in range(start_num, end_num + 1)], 200)
        
        masks_route = category_dir + '/masks'
        masks_train_route = output_dir + '/' + file + '/masks/train'
        if not os.path.exists(masks_train_route):
                os.makedirs(masks_train_route)
        masks_val_route = output_dir + '/' + file + '/masks/val'
        if not os.path.exists(masks_val_route):
                os.makedirs(masks_val_route)
        rgb_route = category_dir + '/rgb'
        rgb_train_route = output_dir + '/' + file + '/rgb/train'
        if not os.path.exists(rgb_train_route):
                os.makedirs(rgb_train_route)
        rgb_val_route = output_dir + '/' + file + '/rgb/val'
        if not os.path.exists(rgb_val_route):
                os.makedirs(rgb_val_route)
        
        masks_images = os.listdir(masks_route)
        rgb_images = os.listdir(rgb_route)
        
        for img in masks_images:
            if int(img[:-4]) in index:
                os.rename(masks_route + '/' + img, masks_val_route + '/'+ img)
                os.rename(rgb_route + '/' + img[:-3] + 'jpg', rgb_val_route + '/'+ img[:-3] + 'jpg')
            else:
                os.rename(masks_route + '/' + img, masks_train_route + '/'+ img)
                os.rename(rgb_route + '/' + img[:-3] + 'jpg', rgb_train_route + '/'+ img[:-3] + 'jpg')