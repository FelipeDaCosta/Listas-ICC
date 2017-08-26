n = int(input())
maior = 0
menor = 0
for i in range(n):
    a, b = [int(x) for x in input().split()]
    a = a if a%2 != 0 else a + 1
    soma = 0
    for j in range(b):
        soma += a+(j*2)
    if soma > maior or i == 0:
        maior = soma
    if soma < menor or i == 0:
        menor = soma
    print(soma)
print(maior)
print(menor)
    
        
