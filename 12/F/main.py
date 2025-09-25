n, m =  map(int, input().split())
arr = [[int(j) for j in input().split()] for i in range(1, n + 1)]
x = int(input())
hon = [[int(x) for x in input().split()] for st in range(x)]
summ = 0
for s in range(x):
    kx = hon[s][0]
    ky = hon[s][1]
    summ += arr[kx - 1][ky - 1]
    arr[kx - 1][ky - 1] = 0
print(summ)