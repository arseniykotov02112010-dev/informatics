n, m = map(int, input().split())
arr = [[int(j) for j in input().split()]for i in range(n)]
sum_num = 0
sum_len = 0
for x in arr:
    sum_num += sum(x)
med_res = sum_num / (n * m)
res_matr = [[0 for j in range(m)]for i in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] > med_res:
            res_matr[i][j] =  1
print(med_res)
for d in res_matr:
    print(*d)