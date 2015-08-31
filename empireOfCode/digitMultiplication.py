


def golf1(d):
 t=1
 r=[x for x in `d` if x!="0"]
 for x in r:t*=int(x)
 return t

def golf(d):
 t=1
 for l in str(d):
  if l!="0":t*=int(l)
 return t

#
if __name__ == '__main__':
 # These "asserts" using only for self-checking and not necessary for auto-testing
 assert golf(123405) == 120
 assert golf(999) == 729
 assert golf(1000) == 1
 assert golf(1111) == 1
 print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
