import os

import shutil
import datetime

where = "J:/"
what = "test"

try:
    os.listdir(where)
except:
    print("cannot list it")



def findfile(where, name):
    #print("findfile on", where)
    results = []
    if(os.path.isfile(where)):
        raise Exception("cannot find file on a file...")
    content = []
    try:
        content = os.listdir(where)
    except:
        return content
    for elem in content:
        elempath = where+"/"+elem
        if(os.path.isfile(elempath)): # file
            if(elem.lower().find(name.lower()) != -1):
                results.append(elempath)
        elif(os.path.isdir(elempath)): # folder
            results.extend(findfile(elempath, name))
        else:
            print("not a file nor a folder : ", elempath)
    return results


beforeSearch = datetime.datetime.now()
print("search", what, "in", where)

results = findfile(where, what)
print("search took:"
      ,(datetime.datetime.now() - beforeSearch))

print("entries:", len(results))

#for entry in results:
#    print (entry)


