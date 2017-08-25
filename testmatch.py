import random

A = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
F = [{"a", "b"}, {"a", "c"}, {"a", "d"}, {"a", "e"}, {"a", "f"}, {"a", "g"}, {"a", "h"}, {"a", "i"}]

def match(A, B):
    nbfail = 0
    while len(A) > 1:
        if(nbfail > 10):
            return False
        b1 = A[0]
        b2 = A[1]
        if({b1, b2} in F):
            nbfail += 1
            continue
        B.append({b1, b2})
        A = A[2:]
    return True

B = []
copyA = A[:]
random.shuffle(A)

while(match(copyA, B) == False):
    copyA = A[:]
    random.shuffle(copyA)
    B = []
    pass

for tuple in B:
    print (tuple)
