import pickle
import urllib
import urllib.request
import re


content = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")

unpacked = pickle.load(content)

for line in unpacked:
    for tuple in line:
        print(tuple[0]*tuple[1], end="")
    print("")
    #print (''.join(map(lambda pair: pair[0]*pair[1], line)))
        
