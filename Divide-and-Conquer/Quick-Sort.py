import random

def compare(x, y):
    global K
    if K == 0:  
        return x < y
    else:
        return x > y

def quickSort(arr, low, high):
    if low >= high:
        return
    i, j = low, high
    pivot = arr[random.randrange(low, high+1)]
    while i <= j:
        while compare(arr[i], pivot): i += 1
        while compare(pivot, arr[j]): j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    quickSort(arr, low, j)
    quickSort(arr, i, high)

#---------------------------------------
  
n, K = map(int, input().strip().split())
arr = [int(x) for x in input().strip().split()]
quickSort(arr, 0, n-1)

for i in range(n):
    print(arr[i], end = ' ')