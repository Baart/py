def golf(p):
 U=L=N=T=0
 for c in p:
  c=ord(c)
  T+=1
  if c>96:L=1
  elif c<64:N=1
  else:U=1
 return U*L*N and T>9


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print golf("ULFFunH8ni")
    #golf('A1213pokl') == False
    #golf('bAse730onE') == True
    #golf('asasasasasasasaas') == False
    #golf('QWERTYqwerty') == False
    #golf('123456123456') == False
    #golf('QwErTy911poqqqq') == True
    #print("Use 'Check' to earn sweet rewards!")
