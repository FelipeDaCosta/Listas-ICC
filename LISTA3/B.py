total = 0
maior = 0
contador = 0
c = int(input())
while c != 0:
    if c > maior or contador == 0:
        maior = c
    total += c
    contador += 1
    c = int(input())
print(contador)
print(maior)
print('%.2f' % (total/contador))
    
