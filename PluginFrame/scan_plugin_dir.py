# -*- coding: utf-8 -*-
"""
Created on Fri May 17 10:33:05 2019

@author: tingliu
"""

import os 


def Test1(rootDir): 
    list_dirs = os.walk(rootDir) 
    for root, dirs, files in list_dirs: 
        for d in dirs: 
            print (os.path.join(root, d))      
        for f in files: 
            print (os.path.join(root, f)) 
