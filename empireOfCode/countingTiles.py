import math
M=math
O=pow
R=range
d=lambda x,y,r:M.sqrt(O(x,2)+O(y,2))<=r
def golf(r):
 P=C=0
 c=int(M.ceil(r))
 for y in R(c):
  for x in R(c):
   s=d(x,y,r)+d(x+1,y,r)+d(x,y+1,r)+d(x+1,y+1,r)
   if s==4:C+=1
   elif s>0:P+=1
 return C*4,P*4

def golf2(r):
 P=C=0
 c=int(M.ceil(r))
 for y in R(c):
  for x in R(c):
   s=d(x,y,r)+d(x+1,y,r)+d(x,y+1,r)+d(x+1,y+1,r)
   if s==4:C+=1
   elif s>0:P+=1
 return C*4,P*4
def golf(r):
 P=C=0
 c=int(M.ceil(r))
 K=[d(x,y,r)+d(x+1,y,r)+d(x,y+1,r)+d(x+1,y+1,r) for y in R(c) for x in R(c)]
 return [a for a in K if a==4].count(4)*4,len([a for a in K if a!=4 and a!=0])*4




if __name__ == '__main__':
 # These "asserts" using only for self-checking and not necessary for auto-testing
 #assert isinstance(golf(1), (list, tuple))
 #assert list(golf(2)) == [4, 12]
 #assert list(golf(3)) == [16, 20]
 assert list(golf(4)) == [32, 28]
 assert list(golf(2.1)) == [4, 20]
 assert list(golf(2.5)) == [12, 20]
 print("All done? Earn rewards by using the 'Check' button!")
