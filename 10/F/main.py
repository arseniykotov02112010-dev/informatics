lis = list(map(int, input().split()))
ln = list()
for i in range (len(lis)):
    if lis[i] > 0:
        ln.append(lis[i])
a = min(ln)
print(a)

