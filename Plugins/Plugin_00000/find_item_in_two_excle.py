#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   find_item_in_two_excle.py
@Time    :   2019/12/08 12:33:57
@Author  :   kejoy 
@Version :   1.0
@Contact :   guangming86@gmail.com
@License :   (C)Copyright 2017-2019, IMMC
@Desc    :   None
'''

# here put the import lib




import xlrd
import os
import sys



def read_xl_file(file_dir):
    xl_file = []
    for root, dirs, files in os.walk(file_dir):
        '''
        print(s + root)        
        print(dirs)
        print(files)
        '''
        for i in files:
            s = i.split('.')
            file_type = str(s[-1])
            #print(file_type)
            #'''
            upper = file_type.upper()
            #print(upper)

            if upper == 'XLS':
                xl_file.append(i)
            elif upper == 'XLSX':
                xl_file.append(i)
            else:
                pass
            #'''
    return xl_file




if __name__ == "__main__":
    file_dir = sys.path[0]
    xl_file = read_xl_file(file_dir)
    print(xl_file)
    
