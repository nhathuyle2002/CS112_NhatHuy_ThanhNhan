# nhathuy

import sys
sys.stdin = open("input.txt")

N, S = map(int, input().strip().split())
a = list(map(int, input().strip().split()))

MAXD = 3000
inf = int(1e10)

maxValue = max(a)
result = 0

if S > MAXD:
    result = (S - MAXD) // maxValue + ((S - MAXD) % maxValue == 0)
    S = S - result * maxValue

f = [inf] * (S+1)
f[0] = 0

for x in a:
    for i in range(x, S+1):
        f[i] = min(f[i], f[i - x] + 1)

result += f[S];
print(result)