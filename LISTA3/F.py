a = int(input())
b = int(input())

while a%b != 0:
    r = a%b
    a = b
    b = r

print(b)
