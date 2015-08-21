



def s1(p):
 r=[(ord(l) - 96) for l in p if not l.isupper()]
 t=[(ord(l.lower()) - 96)*1.5 for l in p if l.isupper()]
 return sum(r+t)
#print s1(raw_input())


e="cab" #raw_input()
print sum([(ord(l)-64) for l in e if not l.isupper()]+[(ord(l.lower())-96)*1.5 for l in e if l.isupper()])



def s2(p):
 c=0
 for l in p:
  if l.isupper():
   c+=(ord(l.lower())-96)*1.5
  else:
   c+=ord(l)-96
 return c
#print s(raw_input())






assert(s1('abc') == 6)
assert(s1('Cab') == 7.5)

#assert(s2('abc') == 6)
#assert(s2('Cab') == 7.5)
