n, m = map(int, input().split())
arr = [[int(j) for j in input().split()] for i in range(n)]
res =[]
for j in range(m):
    res1 = []
    for i in range(n):
        res1.append(arr[i][j])
    res.append(res1)
for x in res:
    print(*x)