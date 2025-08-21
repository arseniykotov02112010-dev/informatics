n = int(input())
for _ in range(n - 1):
    print('+___', end=' ')
print('+___')
for i in range(1, n):
    print(f'|{i} /', end=' ')
print(f'|{n} /')
for _ in range(n - 1):
    print('|__\\ ', end="")
print('|__\\ ')
for _ in range(n - 1):
    print('|   ', end=' ')
print('|   ', end='')