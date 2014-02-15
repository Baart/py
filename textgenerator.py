import random

mytable = {}

with open("D:/test/input.txt") as textfile:
    prev1 = ""
    prev2 = ""
    for line in textfile:
        words = line.split()
        for word in words:
            index = prev1+" "+prev2
            try:
                mytable[index]
            except:
                mytable[index] = []                
            mytable[prev1+" "+prev2].append(word)
            prev1 = prev2
            prev2 = word

prev1=""
prev2=""

finaltext = ""

for i in range(100):
    try:
        mytable[prev1+" "+prev2]
    except:
        break;
    wordlist = mytable[prev1+" "+prev2]
    word = wordlist[random.randrange(0, len(wordlist))]
    finaltext += word + " "
    prev1 = prev2
    prev2 = word

print(finaltext)
