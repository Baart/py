import math
import itertools
O=math.pow
Q=math.fabs
k=lambda hole, lastPoint: math.sqrt(math.pow(math.fabs(hole[1]-lastPoint[1]),2)+math.pow(math.fabs(hole[0]-lastPoint[0]),2))
def golf(holes):
    total=999
    for i in range(0, len(holes)+1):
        for subset in itertools.permutations(holes, i):
            if len(subset) == 5:
                lastPoint=(0,0)
                a=99
                t=0
                for hole in subset:
                    t+=k(hole, lastPoint)
                    lastPoint=hole
                if t < total: total=t
    return total


import itertools as o
def golf(H):
 T=999
 for i in range(6):
  for S in o.permutations(H,i):
   if len(S)!=5:continue
   l=(0,0)
   a=99
   t=0
   for h in S:
    t+=((h[1]-l[1])**2+(h[0]-l[0])**2)**0.5
    l=h
   if t<T:T=t
 return T




if __name__ == '__main__':
 # These "asserts" using only for self-checking and not necessary for auto-testing
 def almost_equal(checked, correct, significant_digits=2):
  precision = 0.1 ** significant_digits
  return correct - precision < checked < correct + precision
 assert almost_equal(golf({(2, 2), (2, 8), (8, 8), (8, 2), (5, 5)}), 23.31)
 assert almost_equal(golf({(2, 2), (4, 4), (6, 6), (8, 8), (9, 9)}), 12.73)
 assert almost_equal(golf({(3, 8), (5, 1), (6, 2), (9, 9), (7, 7)}), 20.17)
 print("Earn cool rewards by using the 'Check' button!")
