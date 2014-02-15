import urllib.request
import zipfile
import os
import re

zipname = "channel.zip"

myzip = ""

if not os.path.isfile(zipname):
    response = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/channel.zip")
    with open(zipname, "wb") as myzip:
        myzip.write(response.read())

if not os.path.exists("extract"):
    os.makedirs("extract")

myzip = zipfile.ZipFile(zipname)

if (len(os.listdir("extract")) == 0):
    myzip.extractall("extract/")

print(myzip.getinfo("90052.txt").comment)


filename = "extract/90052.txt"

count = 0
history = []
while 1:
    with open(filename) as f:
        count+=1
        lines = f.readlines()
        try:
            nextfield = re.findall("\d+", lines[0])[0]
            filename = "extract/"+nextfield+".txt"
            comment = myzip.getinfo(nextfield+".txt").comment
            #print(":",comment)
            history.append(str(comment))
        except:
            #print('->'.join(lines))
            break;

for i in history:
    print(str(i)[2], end="")
#print(''.join([history for i in history]))
print("total ", len(os.listdir("extract")), "files")
print("parsed", count, "files")
#for file in os.listdir("extract"):
#    print(file)




