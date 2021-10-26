import math

SIZE = 9
SMALL_SIZE = int(math.sqrt(SIZE))
step = 0


def initialize():
    global dRow
    global dColumn
    global dSquare
    dRow = [[0 for x in range(0, SIZE+1)] for i in range(0, SIZE)]
    dColumn = [[0 for x in range(0, SIZE+1)] for i in range(0, SIZE)]
    dSquare = [[[0 for x in range(0, SIZE+1)] for i in range(0, SMALL_SIZE)] for j in range(0, SMALL_SIZE)]

    for i in range(0, SIZE):
        for j in range(0, SIZE):
            dRow[i][mat[i][j]] += 1
            dColumn[j][mat[i][j]] += 1
            dSquare[i//SMALL_SIZE][j//SMALL_SIZE][mat[i][j]] += 1

#--------------------------

def calc(i, j):
    global step
    step += 1
    if step > 1e6:
        print("None")
        exit()

    if (i == SIZE):
        return True

    if mat[i][j] != 0: 
        if calc(i + (j+1)//SIZE, (j+1) % SIZE):
            return True
    elif mat[i][j] == 0:
        for x in range(1, SIZE+1):
            if dRow[i][x] == 0 and dColumn[j][x] == 0 and dSquare[i//SMALL_SIZE][j//SMALL_SIZE][x] == 0:
                mat[i][j] = x
                dRow[i][x] += 1
                dColumn[j][x] += 1
                dSquare[i//SMALL_SIZE][j//SMALL_SIZE][x] += 1
                if calc(i + (j+1)//SIZE, (j+1) % SIZE):
                    return True
                dRow[i][x] -= 1
                dColumn[j][x] -= 1
                dSquare[i//SMALL_SIZE][j//SMALL_SIZE][x] -= 1
        mat[i][j] = 0
    return False

#-------------------

mat = [[int(j) for j in input().strip().split()] for i in range(0, SIZE)]

initialize()

if calc(0, 0) == False:
    print("None")
else:
    for i in range(0, SIZE):
        for j in range(0, SIZE):
            print(mat[i][j], end=' ')
        print(end='\n')
        


    