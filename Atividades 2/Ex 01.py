import random

numero_d0_pc = random.randint(0, 10)

chute = 0
while chute != numero_d0_pc:
    chute = int(input("Adivinhe o número: "))
print("Você acertou!")

print("nossa você precisou de {} palpite para vencer.".format(chute))