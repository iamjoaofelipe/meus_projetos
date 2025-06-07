import random

numero_secreto = random.randint(1, 10)
tentativas = 3

print("Tente adivinhar um número secreto entre 1 e 10!")
print(f"Você tem {tentativas} tentativas.")

for i in range(tentativas):
    palpite = int(input("Digite seu palpite: "))

    if palpite == numero_secreto:
        print("Parabéns, você acertou!")
        break
    else:
        print("Errado!")
        if palpite < numero_secreto:
            print("Dica: Tente um número maior.")
        else:
            print("Dica: Tente um número menor.")

# Só será executado se o jogador não acertar nenhuma tentativa
else:
    print(f"Suas tentativas acabaram. O número secreto era {numero_secreto}.")

















