t = int(input())
for i in range(t):
    a, b = [int(x) for x in input().split()]
    total = 0
    for j in range(b):
        print(a+j, end=' ' if j != b - 1 else '\n')
        total += a+j
    print(total)
        
    
