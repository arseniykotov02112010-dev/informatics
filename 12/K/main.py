n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
step = [[arr[n - i - 1][j] for j in range(n)] for i in range(n)]
result = [[step[n - 1 - j][n - i - 1] for j in range(n)]for i in range(n)]
for x in result:
    print(*x)