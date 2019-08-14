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
import pythoncom
import time
from ctypes import *



#创建对象连接 swapp = win32com.client.Dispatch("sldworks.Application")
def start_sld():
    global swapp
    swapp = win32com.client.Dispatch("sldworks.Application") 
    swapp.visible = 0

start_sld()
swapp.visible = 1
part = swapp.ActiveDoc
str_path_name = r"L:\WorkSpace\solidworks-macro\修改草图尺寸-更新三维模型.SLDPRT"
erros = create_string_buffer("0x00",2048)
warnings = create_string_buffer("0x00",2048)

#Open_doc.argtypes = (str_path_name, c_int(1),c_int(0),c_void_p)
part = swapp.OpenDoc6(str_path_name, c_int(1), c_int(0), "", erros, warnings)
