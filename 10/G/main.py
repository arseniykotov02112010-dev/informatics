ls = list(map(int, input().split()))
height = int(input())
for i in range(len(ls)):
    if height > ls[i]:
        print(i + 1)
        exit()
print(len(ls) + 1)