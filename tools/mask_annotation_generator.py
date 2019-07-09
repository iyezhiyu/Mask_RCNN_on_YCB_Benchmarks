#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 20:44:54 2019

@author: zhiyu
"""

from PIL import Image
import numpy as np
from shapely.geometry import Polygon, MultiPolygon
import cv2



def create_sub_mask_annotation(sub_mask, image_id, category_id, annotation_id, is_crowd):
    # Find contours (boundary lines) around each sub-mask
    # Note: there could be multiple contours if the object
    # is partially occluded. (E.g. an elephant behind a tree)
    imgray = cv2.cvtColor(sub_mask,cv2.COLOR_BGR2GRAY)
    contours, hierarchy = cv2.findContours(imgray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    # For the contours of the instances in the binary images, if its parent is background (hierarchy == 0),
    # then this contour is the mask contour, abandoning the contours whose parent is not background.
    valid_contours = []
    for k in range(len(hierarchy[0])):
        if hierarchy[0][k][3] == 0:
            contour = contours[k].reshape((len(contours[k]), 2))
            valid_contours.append(contour)
    
    
    segmentations = []
    polygons = []
    for contour in valid_contours:

        # Make a polygon and simplify it
        poly = Polygon(contour)
        poly = poly.simplify(1.0, preserve_topology=True)
        polygons.append(poly)
        segmentation = np.array(poly.exterior.coords).ravel().tolist()
        segmentations.append(segmentation)

    # Combine the polygons to calculate the bounding box and area
    multi_poly = MultiPolygon(polygons)
    x, y, max_x, max_y = multi_poly.bounds
    width = max_x - x
    height = max_y - y
    bbox = (x, y, width, height)
    area = multi_poly.area

    annotation = {
        'segmentation': segmentations,
        'iscrowd': is_crowd,
        'image_id': image_id,
        'category_id': category_id,
        'id': annotation_id,
        'bbox': bbox,
        'area': area
    }

    return annotation