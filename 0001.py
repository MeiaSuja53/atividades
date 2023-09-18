def par_ou_impar(numero):
    if numero % 2== 0:
        print(f'0 numero {numero} e par')
    else:
        print(f'0 numero {numero} e impar.')

while True:
    par_ou_impar(int(input('digite o numero inteiro: ')))
    