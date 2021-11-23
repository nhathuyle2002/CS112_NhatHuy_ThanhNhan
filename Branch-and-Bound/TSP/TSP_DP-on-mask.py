N = int(input())
weight = [[int(x) for x in input().strip().split()] for i in range(N)]

#----------------------------------------#

def getBit(x, i):
    return (x >> i) & 1

def changeBit(x, i):
    return x ^ (1 << i)

def solve():
    DP[1][0] = 0
    for x in range(shlN):
        for u in range(N):
            if getBit(x, u) == 1 and DP[x][u] != INF:
                for v in range(N):
                    if getBit(x, v) == 0:
                        y = changeBit(x, v)
                        if DP[y][v] > DP[x][u] + weight[u][v]:
                            DP[y][v] = DP[x][u] + weight[u][v]

    result = INF
    for u in range(1, N):
        if result > DP[shlN - 1][u] + weight[u][0]:
            result = DP[shlN - 1][u] + weight[u][0]

    print(result)

#----------------------------------------#

INF = int(1e9) + 100
shlN = 1 << N
DP = [[INF for i in range(N)] for x in range(shlN)]
solve()