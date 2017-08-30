a = input().strip()
b = input().strip()

if a == b:
    print('-1')
else:
    print(max(len(a), len(b)))
    
