"""
def golf1(matrix):

    minX=idxX=minY=idxY=9999
    for idx,line in enumerate(matrix):
        if sum(line) < minX:
            minX = sum(line)
            idxX = idx

    for x in range(len(matrix[0])):
        line=0
        for y in range(len(matrix)):
            line += matrix[y][x]

        if line < minY:
            minY = line
            idxY = x

    print "weak line is", minX, idxX, minY, idxY
    return [idxX, idxY]
"""

def golf(m):
 A=map(sum,m)
 X=A.index(min(A))
 B=[]
 for x in range(len(m)):
  B.append(sum([t[x]for t in m]))
 Y=B.index(min(B))
 return [X,Y]


if __name__ == '__main__':
  # These "asserts" using only for self-checking and not necessary for auto-testing
 assert golf([[7, 2, 7, 2, 8],
              [2, 9, 4, 1, 7],
              [3, 8, 6, 2, 4],
              [2, 5, 2, 9, 1],
              [6, 6, 5, 4, 5]]) == [3, 3]
 assert golf([[7, 2, 4, 2, 8],
              [2, 8, 1, 1, 7],
              [3, 8, 6, 2, 4],
              [2, 5, 2, 9, 1],
              [6, 6, 5, 4, 5]]) == [1, 2]
 print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
