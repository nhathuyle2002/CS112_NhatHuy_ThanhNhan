
matD = [[1, 1], [1, 0]]
matI = [[1, 0], [0, 1]]
MOD = 132864579

def multiply(a, b):
    c = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % MOD
    return c

def power(a, b):
    if b == 0:
        return matI
    c = power(a, b//2)
    c = multiply(c, c)
    if b%2 == 1:
        c = multiply(c, a)
    return c

def getFibo(i):
    c = power(matD, i)
    return c[0][0]

n = int(input())
a = [int(x) for x in input().strip().split()]

for x in a:
    print(getFibo(x), end=' ')