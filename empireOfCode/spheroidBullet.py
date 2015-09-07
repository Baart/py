import math as m
S=m.sqrt
P=m.pi*2
R=round
def golf(h,w):
 c,a=h/2.,w/2.
 b=a**2
 d=c**2
 if c<a:
  E=1-d/b
  e=S(E)
  d=P*b*(1+(1-E)/e*m.atanh(e))
 elif c>a:
  E=1-b/d
  e=S(E)
  d=P*b*(1+c/(a*e)*m.asin(e))
 else:d=2*P*d
 return R(2*P/3.*b*c,2),R(d,2)

if __name__ == '__main__':
 # These "asserts" using only for self-checking and not necessary for auto-testing

 assert list(golf(2, 4)) == [16.76, 34.69]
 assert list(golf(2, 2)) == [4.19, 12.57]
 assert list(golf(4, 2)) == [8.38, 21.48]
 print("All set? Click 'Check' to review your code and earn rewards!")

"""
 import math
 def golf(height, width):
     c = height / 2.0
     a = width / 2.0
     surface = 0.0
     if c < a: # use oblate formula
         e_square = 1 - c**2/a**2
         e = math.sqrt(e_square)
         surface = (2 * math.pi * a**2) * (1 + ((1-e_square)/e) * math.atanh(e) )
     elif c > a: # use prolate formula
         e_square = 1 - a**2/c**2
         e = math.sqrt(e_square)
         surface = 2 * math.pi * a**2 * (1 + (c/(a*e))* math.asin(e) )
     else: # sphere
         surface = 4 * math.pi * c**2
     volume = 4 * math.pi / 3. * a**2 * c
     return round(volume, 2), round(surface, 2)


     """
