#import winsound

from winsound import Beep
from time import sleep


#for x in xrange(1,100):
#    winsound(100 * x,100)


t= [
(440, 500),
(440, 500),
(440, 500),
(349, 350),
(523, 150),
(440, 500),
(349, 350),
(523, 150),
(440, 1000,),
(659, 500),
(659, 500),
(659, 500),
(698, 350),
(523, 150),
(415, 500),
(349, 350),
(523, 150),
(440, 1000)
]


for f,l in t:
    Beep(f,l)


