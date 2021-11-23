# Le Nhat Huy

S, K, N = map(int, input().strip().split())
A = [[int(x) for x in input().strip().split()] for i in range(N)]

inf = 1e9 + 100
preScore = [[inf for x in range(S+1)] for j in range(K)]

#-----------------------------------#

def solve():
    for j in range(K):
        if j == 0:
            for i in range(N):
                if A[i][0] <= S:
                    preScore[0][A[i][0]] = A[i][0]
            continue

        for i in range(N):
            for x in range(A[i][j], S+1):
                if preScore[j-1][x-A[i][j]] <= A[i][j] and preScore[j][x] > A[i][j]:
                    preScore[j][x] = A[i][j] 
    if preScore[K-1][S] != inf:
        return True
    else:
        return False

#-----------------------------------#

if solve():
    print("YES") 
else:
    print("NO")
