st = input()
x = len(st) // 2
if len(st) % 2 != 0:
    x += 1
res = st[x:len(st)] + st[:x]
print(res)