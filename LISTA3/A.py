n = int(input())
c = int(input())
while c != n:
    if c > n:
        print("O número correto é menor.")
    elif c < n:
        print ("O número correto é maior.")
    c = int(input())
print("Parabéns! Você acertou.")
