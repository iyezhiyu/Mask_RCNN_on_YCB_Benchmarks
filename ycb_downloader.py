#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 19:55:57 2019

@author: zhiyu
"""
"""
Use the classes below:
    002_master_chef_can
    003_cracker_box
    004_sugar_box
    005_tomato_soup_can
    006_mustard_bottle
    007_tuna_fish_can
    008_pudding_box
    009_gelatin_box
    010_potted_meat_can
    011_banana
    019_pitcher_base
    021_bleach_cleanser
    024_bowl
    025_mug
    035_power_drill
    036_wood_block
    037_scissors
    040_large_marker
    051_large_clamp
    052_extra_large_clamp
    061_foam_brick

The route for the 025_mug has problems, so after finishing this program,
we should manually change the location of the 025_mug.
"""

import os
from urllib import request
import tarfile
import re

rooturl = "http://ycb-benchmarks.s3-website-us-east-1.amazonaws.com"
html = request.urlopen(rooturl)
doc = html.read().decode('utf-8')
html.close()
tlinks = re.findall(r'href\=\"([a-zA-Z0-9\.\/\_\-]+)rgbd.tgz\"', doc)
for i in range(len(tlinks)):
    tlinks[i]= rooturl + '/' + tlinks[i] + 'rgbd.tgz'

links = []
links.append(tlinks[1]) # 002_master_chef_can
links.append(tlinks[2]) # 003_cracker_box
links.append(tlinks[3]) # 004_sugar_box
links.append(tlinks[4]) # 005_tomato_soup_can
links.append(tlinks[5]) # 006_mustard_bottle
links.append(tlinks[6]) # 007_tuna_fish_can
links.append(tlinks[7]) # 008_pudding_box
links.append(tlinks[8]) # 009_gelatin_box
links.append(tlinks[9]) # 010_potted_meat_can
links.append(tlinks[10]) # 011_banana
links.append(tlinks[18]) # 019_pitcher_base
links.append(tlinks[19]) # 021_bleach_cleanser
links.append(tlinks[22]) # 024_bowl
links.append(tlinks[23]) # 025_mug
links.append(tlinks[31]) # 035_power_drill
links.append(tlinks[32]) # 036_wood_block
links.append(tlinks[33]) # 037_scissors
links.append(tlinks[36]) # 040_large_marker
links.append(tlinks[46]) # 051_large_clamp
links.append(tlinks[47]) # 052_extra_large_clamp
links.append(tlinks[55]) # 061_foam_brick


output_dir = '/mnt/disk/zhiyu/ycb_objects'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for url in links:
    filename = url[url[:url.rindex('/')].rindex('/')+1:url.rindex('/')]+'.tgz'
    url_out = os.path.join(output_dir, filename)
    print("Downloading", filename)
    request.urlretrieve(url, url_out)
    print("Downloading", filename, "finished")
    print("Extracting", filename)
    tar = tarfile.open(url_out)
    names = tar.getnames()
    for name in names:
        tar.extract(name, path=output_dir)
    tar.close()
    print("Extracting", filename, "finished")
    os.remove(url_out)
    
print("All downloading and extracting finished")