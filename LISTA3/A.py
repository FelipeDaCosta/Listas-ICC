n = int(input())
c = int(input())
while c != n:
    if c > n:
        print("O número correto e menor.")
    elif c < n:
        print ("O numero corretóe maior.")
    c = int(input())
print("Parabens! Voce acertou.")
