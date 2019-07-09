#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 01:30:53 2019

@author: zhiyu
"""
"""
The aim of this program is to rename all the images.
"""

import os

input_dir = 'path to/ycb_preprocessed'
output_dir = 'path to/ycb_renamed'

newnames = {'002_m': 1, '003_c': 2, '004_s': 3, '005_t': 4, '006_m': 5,\
            '007_t': 6, '008_p': 7, '009_g': 8, '010_p': 9, '011_b': 10,\
            '019_p': 11, '021_b': 12, '024_b': 13, '025_m': 14, '035_p': 15,\
            '036_w': 16, '037_s': 17, '040_l': 18, '051_l': 19, '052_e': 20,\
            '061_f': 21}

files = os.listdir(input_dir)
for file in files:
    category_dir = input_dir+'/'+file
    if os.path.isdir(category_dir):
        category_id = newnames[file[:5]]
        new_category_dir_name = str(category_id)
        if len(new_category_dir_name) == 1:
            new_category_dir_name = '0' + new_category_dir_name
        new_category_dir_name = new_category_dir_name + file[3:]
        masks_route = category_dir + '/' + 'masks'
        rgb_route = category_dir + '/' + 'rgb'
        masks_images = os.listdir(masks_route)
        rgb_images = os.listdir(rgb_route)
        
        new_masks_route = output_dir + '/' + new_category_dir_name + '/' + 'masks'
        new_rgb_route = output_dir + '/' + new_category_dir_name + '/' + 'rgb'
        if not os.path.exists(new_masks_route):
                os.makedirs(new_masks_route)
        if not os.path.exists(new_rgb_route):
                os.makedirs(new_rgb_route)
        
        count = 0
        for img in masks_images:
            mask_oldname = masks_route + '/' + img
            mask_newname = new_masks_route + '/' + str((category_id - 1) * 600 + count) + '.pbm'
            rgb_oldname = rgb_route + '/' + img[:-9] + '.jpg'
            rgb_newname = new_rgb_route + '/' + str((category_id - 1) * 600 + count) + '.jpg'
            os.rename(mask_oldname, mask_newname)
            os.rename(rgb_oldname, rgb_newname)
            count = count + 1