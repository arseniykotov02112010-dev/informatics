n = int(input())
arr = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if i + j == n- 1:
            arr[i][j] = 1
        elif i + j > n - 1:
            arr[i][j] = 2
        else:
            arr[i][j] = 0
for x in arr:
    print(*x)
