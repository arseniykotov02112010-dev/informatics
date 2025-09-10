lis = list(map(int, input().split()))
cnt = 0
for i in range(1, len(lis) - 1):
    if lis[i] > lis[i - 1] and lis[i] > lis[i + 1]:
        cnt += 1
print(cnt)