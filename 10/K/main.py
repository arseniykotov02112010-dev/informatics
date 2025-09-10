ls = list(map(int, input().split()))
cnt1 = 0
for char in ls:
    cnt2 = ls.count(char)
    if cnt2 > cnt1:
        cnt1 = max(cnt1, cnt2)
        res_ind = ls.index(char)
print(ls[res_ind])