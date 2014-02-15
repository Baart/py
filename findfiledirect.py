# -*- coding: utf-8 -*- 

import sys
import os

print "tst"

def listpath(path, searchstr):
    for elem in os.listdir(path):
        fullpath = path+"/"+elem
        if(os.path.isfile(fullpath)):
            if(elem.find(searchstr) != -1):
                pass
                #print(fullpath)
        if(os.path.isdir(fullpath)):
            listpath(fullpath, searchstr)

#listpath("C:/MinGW", "bat")
