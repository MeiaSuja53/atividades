def nm_5 (numero):
    if numero % 5 == 0:
        print(f'O numero {numero} é multiplo de 5')
    else:
        print(f'O numero {numero} é multiplo de 5')

def nm_3 (numero):
    if numero % 3 == 0:
        print(f'O numero {numero} é multiplo de 3')
    else:
        print(f'O numero {numero} é multiplo de 3')

numero = int(input('Digite u, número inteiro: '))
if nm_5(numero) and nm_3(numero):
    print(f'O número {numero} é multiplo de 3 e de 5.')
elif nm_5(numero):
    print(f'O número {numero} é multiplo de 5.')
elif nm_3(numero):
    print(f'O número {numero} é multiplo de 3.')
else:
    print(f"o numero {numero} não é multiplo de 5 nem de 3.")