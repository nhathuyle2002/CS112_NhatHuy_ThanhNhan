import math
import sys

#sys.stdin = open("input.txt")

minDis = 1e18

def update(a, b):
    global minDis
    minDis = min(minDis, math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2))

def nearestPoint(a, low, high):
    if low == high:
        return
    if low == high-1:
        update(a[low], a[high])
        if a[low][1] > a[high][1]:
            a[low], a[high] = a[high], a[low]
        return 

    mid = (low + high) // 2
    midPoint = a[mid]
    nearestPoint(a, low, mid)
    nearestPoint(a, mid+1, high)

    t = []
    j = mid+1
    for i in range(low, mid+1):
        while j <= high and a[j][1] < a[i][1]:
            t.append(a[j])
            j += 1
        t.append(a[i])
    while j <= high:
        t.append(a[j])
        j += 1

    for i in range(high-low+1):
        a[low+i] = t[i]

    t = []
    for i in range(low, high+1):
        if abs(midPoint[0] - a[i][0]) < minDis:
            j = len(t) -1
            while j >= 0 and abs(a[i][1] - t[j][1]) < minDis:
                update(a[i], t[j])
                j -= 1
            t.append(a[i]) 

#---------------------------------------
  
n = int(input().strip())
a = []
for i in range(n):
    x, y = map(int, input().strip().split())
    a.append((x, y))
a.sort()

nearestPoint(a, 0, n-1)
print(round(minDis, 3))