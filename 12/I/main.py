n, m = map(int, input().split())
arr = [[int(j) for j in input().split()]for i in range(n)]
for i in range(n):
    arr[i] = arr[i][::-1]
for x in arr:
    print(*x)