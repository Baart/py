from __future__ import print_function
from time import sleep

print ("test")
for x in range(101):
    print ("\r " + str(x), end="")
    sleep(0.1)
print ("")
print ("test end")