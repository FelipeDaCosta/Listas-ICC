n = int(input())
fat = 1
a, b = 0, 1
for i in range(1, n+1):
    fat *= i
    if i > 1:
        c = a + b
        a = b
        b = c
if b%2 == 0:
    print(b, fat, a)
else:
    print(b, fat)
