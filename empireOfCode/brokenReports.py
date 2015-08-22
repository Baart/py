import re
def golf2(b):
 return sum([(ord(x[0])-65)*9+int(x[1])for x in re.findall('([A-Z][1-9])',b)])

golf=lambda b: sum([(ord(x[0])-65)*9+int(x[1])for x in re.findall('([A-Z][1-9])',b)])

if __name__ == '__main__':
 # These "asserts" using only for self-checking and not necessary for auto-testing
 assert golf("ASDA1,BB22D01C1") == 31
 assert golf("B1,C2,D3") == 60
 print("Earn cool rewards by using the 'Check' button!")
