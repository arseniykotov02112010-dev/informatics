ls = list(map(int, input().split()))
mn = min(ls)
mx = max(ls)
ind_mn = ls.index(mn)
ind_mx = ls.index(mx)
ls[ind_mx] = mn
ls[ind_mn] = mx
print(*ls)