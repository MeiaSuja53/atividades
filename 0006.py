def nm_user (numero):
    numero = int(input('Insira um número: '))
    if numero % 5 == 0:
        print(f'O numero {numero} é multiplo de 5')
    else:
        print(f'O numero {numero} não é multiplo de 5')

def conta(multiplos):
    lista= []
    for i in range(multiplos+1):
        if conta(i):
         lista.append(1)
    return lista

def sistem_chec():
    multiplos = solicit_muner()
