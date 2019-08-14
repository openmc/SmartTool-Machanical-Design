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

#打开文件 part = swapp.OpenDoc(r"str_path_name", 1)
def open_file(str_path_name):
    '''swapp = win32com.client.Dispatch("sldworks.Application")'''
    time.sleep(1)
    swapp.visible = 1
    part = swapp.ActiveDoc
    #part = swapp.OpenDoc(str_path_name, 1)
    #err = win32com.client.VARIANT(pythoncom.VT_BYREF, None)
    #warn = win32com.client.VARIANT(pythoncom.VT_BYREF, None)
    part = swapp.OpenDoc6(str_path_name, 1, 0, "", err_=Exception, warn_=Exception)

# TODO 以下代码OpenDoc6(str_path_name, 1, 0, "", erros, warnings) 【参数类型不匹配-此方法不可用】
    '''
    #err = create_string_buffer(3)
    #warn = create_string_buffer(3)

    err = c_int(10)
    warn = c_int(20)

    err_warn = [c_int(10), c_int(20)]

    #erros = byref(err)
    #warnings = byref(warn)

    #erros = pointer(err)
    #warnings = pointer(warn)

    #erros = ()
    #warnings = ()


    part = swapp.OpenDoc6(str_path_name, 1, 0, "", err_warn[0], err_warn[1])
    print(err)
    print(warn)
    '''

#对象选择SelectByID2
# C++/CLI   
#System.bool SelectByID2( 
#&   System.String^ Name,
#&   System.String^ Type,
#&   System.double X,
#&   System.double Y,
#&   System.double Z,
#&   System.bool Append,
#&   System.int Mark,
#&   Callout^ Callout,
#&   System.int SelectOption
#) 
#  As Boolean
def Select_object(prt_name,object_name,object_type):
    swapp = win32com.client.Dispatch("sldworks.Application")
    print(type(swapp))
    part = swapp.ActiveDoc
    name = object_name +"@" + prt_name
    call_out = win32com.client.VARIANT(pythoncom.VT_DISPATCH, None)
    boolstatus = part.Extension.SelectByID2(
                                            name, 
                                            object_type, 
                                            0.0, 
                                            0.0, 
                                            0.0, 
                                            False, 
                                            0, 
                                            call_out, 
                                            0
                                            )

    print(boolstatus)
    myDimension = part.Parameter(object_name)
    myDimension.SystemValue = 1

#保存文件
def save_file(str_path_name):
    print("save")

if __name__ == "__main__":
    start_sld()
    new_file_path = r"L:\WorkSpace\solidworks-macro\修改草图尺寸-更新三维模型.SLDPRT"
    open_file(new_file_path)
    
    object_name_ = "D2@草图1"
    prt_name_ = "修改草图尺寸-更新三维模型.SLDPRT"
    object_type_ = "DIMENSION"
    Select_object(object_name_,prt_name_,object_type_)   
