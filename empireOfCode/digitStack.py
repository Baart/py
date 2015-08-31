def golf1(commands):
    stack = []
    sSum = 0
    for cmd in commands:
        if "PUSH" in cmd:
            stack.append(int(cmd.split()[1]))
        if "POP" in cmd:
            if len(stack):
                nb = stack.pop()
                sSum += nb
        if "PEEK" in cmd:
            if len(stack):
                sSum += stack[-1]

    return sSum

def golf(X):
 D=[]
 S=0
 for C in X:
  l=len(D)
  if "PUSH"in C:D.append(int(C[5]))
  if "POP"in C*l:S+=D.pop()
  if "PEEK"in C*l:S+=D[-1]
 return S

if __name__ == '__main__':
# These "asserts" using only for self-checking and not necessary for auto-testing
 assert golf(("PUSH 3", "POP", "POP", "PUSH 4", "PEEK", "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK")) == 8, "Example"
 assert golf(("POP", "POP")) == 0, "PopPop"
 assert golf(("PUSH 9", "PUSH 9", "POP")) == 9, "Push 9"
 assert golf(()) == 0, "Empty"
 print("All done? Earn rewards by using the 'Check' button!")
