s = input()
is_digit = False
for i in s:
    if i.isdigit():
        is_digit = True
if len(s) >= 8 and is_digit and s.upper() != s and s.lower() != s:
    res = 'Yes'
else:
    res = ('No')
print(res)