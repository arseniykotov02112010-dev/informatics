n, m, x, y = map(int, input().split())
xls = list(map(int, input().split()))
yls = list(map(int, input().split()))
if x < y and max(xls) < min (yls) and x < min(yls) and max(xls) < y:
    print('No', end=' ')
print('War')

