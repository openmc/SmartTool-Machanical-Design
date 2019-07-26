#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   solidworks_api.py
@Time    :   2019/07/25 08:53:44
@Author  :   IMMC-kejoy 
@Version :   1.0
@Contact :   guangming86@gmail.com
@License :   (C)Copyright 2019-&&
@Desc    :   None
'''

# the import lib

import win32com.client
import time

#创建对象连接
def start_sld():
    global swapp
    swapp = win32com.client.Dispatch("sldworks.Application") 
    swapp.visible = 1

def save_file(str_path_name):
    print("save")

def open_file(str_path_name):
    open_file = swapp.OpenDoc(r"str_path_name", 1)




start_sld()
time.sleep(10)
swapp.visible = 0
time.sleep(10)
swapp.visible = 1
