n = int(input())
arr = [[int(j) for j in input().split()] for i in range(n)]

# Проверка наличия всех чисел от 1 до N^2
required_numbers = set(range(1, n * n + 1))
actual_numbers = set()
for i in range(n):
    for j in range(n):
        actual_numbers.add(arr[i][j])

if required_numbers != actual_numbers:
    print('No')
    exit(0)

# Проверка сумм строк
first_row_sum = sum(arr[0])
for i in range(1, n):
    if sum(arr[i]) != first_row_sum:
        print('No')
        exit(0)

# Проверка сумм столбцов
column_sums = []
for j in range(n):
    col_sum = 0
    for i in range(n):
        col_sum += arr[i][j]
    column_sums.append(col_sum)

for j in range(1, n):
    if column_sums[j] != column_sums[0]:
        print('No')
        exit(0)

# Проверка главной диагонали
main_diag_sum = 0
for i in range(n):
    main_diag_sum += arr[i][i]

# Проверка побочной диагонали
secondary_diag_sum = 0
for i in range(n):
    secondary_diag_sum += arr[i][n - 1 - i]

# Финальная проверка всех сумм
if first_row_sum == column_sums[0] == main_diag_sum == secondary_diag_sum:
    print('Yes')
else:
    print('No')
'''
n = int(input())
arr = [[int(j) for j in input().split()] for i in range(n)]
a = sum(arr[0])
for x in range(1, n):
    if a != sum(arr[x]):
        print('No')
        quit()
a1 = list()
for j in range(n):
    sum_col = 0
    for i in range(n):
        sum_col += arr[i][j]
    a1.append(sum_col)
sum_a1 = a1[0]
for j in range(1, n):
    if a1[j] != a1[0]:
        print('No')
        quit()
sum_main = 0
for i in range(n):
    sum_main += arr[i][i]
sum_rl = 0
for i in range(n):
    sum_rl += arr[i][n - 1 - i]
if a == a1 == sum_main == sum_rl:
   print('Yes')
else:
    print('No')
'''