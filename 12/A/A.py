n, m = map(int, input().split())
arr = [[1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
for char in arr:
    print(*char)


