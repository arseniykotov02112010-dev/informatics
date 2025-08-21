st = input()
res =''
for i in range (len(st)):
    if i % 3 == 0:
        continue
    res += st[i]
print(res)