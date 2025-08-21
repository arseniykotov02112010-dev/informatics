x = int(input())
x_hours = x // 60
x_min = x % 60
res = f'{x_hours + 9:02d}:{x_min:02d}'
print(res)