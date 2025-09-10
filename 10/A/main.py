'''
a = list(map(int, input().split()))
res = []
for x in range(len(a)):
    if x % 2 == 0:
        res.append(str(a[x]))
print(' '.join(res))
'''
'''
a = list(map(int, input().split()))
for x in range(len(a)):
    if x % 2 == 0:
        print(a[x], end=' ')
'''
a = list(map(str, input().split()))
res = a[::2]
print(' '.join(res))