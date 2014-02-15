import PIL.Image
import random

w = 1200
h = 1200

imgresult = PIL.Image.new("RGBA", (w, h), (0,0,0,255))

for i in range(w):
    for j in range(300,900, 1):
        xy = (i,j)
        imgresult.putpixel(xy, (random.randrange(0,255),
                                random.randrange(0,255),
                                random.randrange(0,255)
                                )
                           )
for i in range(300,900, 1):
    for j in range(h):
        xy = (i,j)
        imgresult.putpixel(xy, (random.randrange(0,255),
                                random.randrange(0,255),
                                random.randrange(0,255)
                                )
                           )
        
imgresult.save("random_image.jpg")

