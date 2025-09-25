n = int(input())
arr = [[int(j) for j in input().split()] for i in range(n)]
res = True
for i in range(n):
    for j in range(n):
        if arr[i][j] != arr[j][i]:
            res = False
print('Yes' if res == True else 'No')
