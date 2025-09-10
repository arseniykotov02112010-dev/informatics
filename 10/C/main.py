res = list()
lis = list(map(int, input().split()))
n1 = lis[0]
for i in range(1, len(lis)):
    n2 = lis[i]
    if n2 > n1:
        res.append(n2)
    n1 = n2
print(*res)
'''
for i in range(1, len(lis)):
    if i[i] > i[i - 1]:
        res.append(i[i])
'''