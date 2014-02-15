import PIL.Image
import urllib.request
import os

imgname = "oxygen.png"

if(not os.path.isfile(imgname)):
    with open(imgname, "wb") as imgfile:
        data = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png")
        imgfile.write(data.read())




imgdata = PIL.Image.open(imgname)
#print(imgdata.getextrema())
#print(imgdata.getdata())
print(imgdata.getbbox())
#print(imgdata.getbands())
#print(imgdata.getcolors())
#print(imgdata.getim())
#print(imgdata.getprojection())
#print(imgdata.histogram())

def colorequal(b, c):
    for e in b:
        print(e)

box = imgdata.getbbox()

lastcolor = (0,0,0,0)
for i in range(box[3]):
    color = imgdata.getpixel((0, i))
    #colorequal(lastcolor, color)
    if(lastcolor == color):
        print("interesting line", i)    
    lastcolor = color

lastcolor = (0,0,0,0)
info = []
for i in range(box[2]):
    color = imgdata.getpixel((i, 48))
    if(lastcolor == color):
        if(color not in info):
            info.append(color)
    lastcolor = color

for color in info:
    print(color[0], end=" ")

print()

for color in info:
    print(chr(color[0]), end=" ")

for char in [1, 0, 5, 6, 3, 4, 2]:
    print(chr(char))


