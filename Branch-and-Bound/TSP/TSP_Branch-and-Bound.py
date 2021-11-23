N = int(input())
if N == 1:
    print(0)
    quit()

weight = [[int(x) for x in input().strip().split()] for i in range(N)]
weightOrderId = [[j for j in range(N)] for i in range(N)]

for u in range(N):
    for i in range(N):
        for j in range(i+1, N):
            if weight[u][weightOrderId[u][i]] > weight[u][weightOrderId[u][j]]:
                weightOrderId[u][i], weightOrderId[u][j] = weightOrderId[u][j], weightOrderId[u][i]

minSum = 0
for i in range(N):
    minSum += weight[i][weightOrderId[i][1]]

def solve(deg, U, curSum, minRestSum):
    global result

    if curSum + minRestSum >= result:
        return

    if deg == N:
        if curSum + weight[U][0] < result:
            result = curSum + weight[U][0]
        return

    for V in weightOrderId[U]:
        if not visited[V]:
            visited[V] = True
            solve(deg + 1, V, curSum + weight[U][V], minRestSum - weight[V][weightOrderId[V][1]])
            visited[V] = False


#----------------------------------------#

visited = [False for i in range(N)]
result = int(1e9) + 100
visited[0] = True
solve(1, 0, 0, minSum)
print(result)