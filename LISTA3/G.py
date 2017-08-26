n = int(input())
r = n + 2 if n <= 2 else n - 2
finish = False
for m in range(1, r+1):
    value = n*m+1
    for i in range(2, value):
        if value % i == 0:
            print(m)
            finish = True
            break
    if finish:
        break
            
