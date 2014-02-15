# -*- coding: utf-8 -*- 

import sys
import os

'''
Iterate throug path and print file that contains requested name 
'''
def listpath(path, searchstr):
    for elem in os.listdir(path):
        fullpath = path+"/"+elem
        if(os.path.isfile(fullpath)):
            if(elem.find(searchstr) != -1):
                print(fullpath)
        if(os.path.isdir(fullpath)):
            listpath(fullpath, searchstr)

listpath("C:/MinGW", "bat")
