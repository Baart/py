import operator


f = open("input.yxy.py")


a=[]
for line in f.readlines():
    a.append(line.split())



for item in a:
    if (len(item) != 3):
        for word in item:
            if (word.isdigit()):
                item[1] = word
            elif("%" in word):
                item[2] = word
            else:
                item[0] += word + " "
        item = item[0:3]


for item in a:
    if (item[1].isdigit()):
        item[1] = int(item[1])
    else:
        item[1] = 0

a = sorted(a, key=operator.itemgetter(1), reverse=True)

maxlength = [0,0,0]
for item in a:
    for i in range(3):
        if(maxlength[i] < len(str(item[i]))+2):
           maxlength[i] = len(str(item[i]))+2

print(maxlength)
for item in a:
    for i in range(3):
        print(str(item[i]) + "-"*( maxlength[i] - len(str(item[i]))), sep="", end="")
    print()
    #print(item[0:3])
    

