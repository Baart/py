import re
f = open("../txt3.txt");

lines = f.readlines()

findit = re.compile("[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}")


final = ""
for line in lines:
    for a in re.findall(findit, line):
        final += a[4]
        print(a[1])
    


print (final)
