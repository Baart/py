# coding=utf-8
import codecs
letters = "stsobteji"
expected = 6



output = []
i = 0
with open("dico.txt", 'r') as f:
    for line in f:
        line = line.strip()
        if len(line) != expected:
            continue
        valid = True
        for letter in line:
            if letter not in letters:
                valid = False
                break

        if valid:
            output.append(line)


print '\n'.join(output)

