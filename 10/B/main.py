a = list(map(int, input().split()))
res = []
for num in a:
    if num % 2 == 0:
        res.append(num)
print(*res)