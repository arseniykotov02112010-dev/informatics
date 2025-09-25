n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        arr[i][j] = m * i + j if i % 2 == 0 else m * i + m - j - 1
for x in arr:
    print(*x)