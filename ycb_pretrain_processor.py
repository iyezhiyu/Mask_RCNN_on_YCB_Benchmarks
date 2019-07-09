#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 22:11:31 2019

@author: zhiyu
"""
"""
This program aims to move all the files to the right place.
"""

import os

input_dir = 'path to/ycb_train_val_splited'
anno_input_dir = 'path to/ycb_annotations'
output_dir = 'path to/ycb_for_train'

files = os.listdir(input_dir)
for file in files:
    category_dir = input_dir+'/'+file
    if os.path.isdir(category_dir):
        train_images = os.listdir(category_dir+'/rgb/train')
        if not os.path.exists(output_dir + '/train'):
                os.makedirs(output_dir + '/train')
        for image in train_images:
            os.rename(category_dir + '/rgb/train/' + image, output_dir + '/train/'+ image)
            
        val_images = os.listdir(category_dir+'/rgb/val')
        if not os.path.exists(output_dir + '/val'):
                os.makedirs(output_dir + '/val')
        for image in val_images:
            os.rename(category_dir + '/rgb/val/' + image, output_dir + '/val/'+ image)


if not os.path.exists(output_dir + '/annotations'):
    os.makedirs(output_dir + '/annotations')
os.rename(anno_input_dir + '/instances_train.json', output_dir + '/annotations/train.json')
os.rename(anno_input_dir + '/instances_val.json', output_dir + '/annotations/val.json')

