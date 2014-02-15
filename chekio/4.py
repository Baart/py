import urllib.request
import re





param = 37278

while 1:
    req = urllib.request.Request(url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+str(param))
    f = urllib.request.urlopen(req)
    line = str(f.read());

    words = line.split()

    myint = [int(x.group()) for x in re.finditer(r'\d+', line)]

    myint = myint[0]
    param = myint
    print(myint)



#s = "546 bl 12.3 abla 5875"
#t = re.findall(r'\d+', s)
