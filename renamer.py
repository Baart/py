# renamer.py

import os
import os.path

def mylist(basepath, match, replace):
    for elem in os.listdir(basepath):
        fullpath = basepath + "/" + elem
        if os.path.isdir(fullpath):
            mylist(fullpath, match, replace)
        elif os.path.isfile(fullpath):
            if match in elem:
                newfilename = elem.replace(match, replace)
                newpath = basepath+"/"+ newfilename
                print elem, "->", newfilename
                os.rename(fullpath, newpath)
        else:
            print(fullpath, "is nothing")







path = "D:/DivX"
search = "-"
replace = "-"



mylist(path, search, replace)
