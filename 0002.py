def nm (numero):
    if numero % 5 == 0:
        print(f'O numero {numero} é multiplo de 5')
    else:
        print(f'O numero {numero} não é multiplo de 5.')

while True:
    nm(int(input('digite o numero inteiro: ')))
    