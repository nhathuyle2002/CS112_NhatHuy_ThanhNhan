# Le Nhat Huy

S, K, N = map(int, input().strip().split())
A = [[int(x) for x in input().strip().split()] for i in range(N)]

#-----------------------------------#

def solve(deg, preScore, curSum):
    if deg >= K:
        if curSum == S:
            return True
        else:
            return False

    for i in range(N):
        if A[i][deg] < preScore:
            continue
        if curSum + A[i][deg] * (K - deg) > S:
            continue
        else:
            if solve(deg + 1, A[i][deg], curSum + A[i][deg]):
                return True
    return False

#-----------------------------------#

if solve(0, 0, 0):
    print("YES") 
else:
    print("NO")