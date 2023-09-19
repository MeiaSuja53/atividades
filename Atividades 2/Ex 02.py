import random
def jokenpo():
    opcoes_do_jogo = ['pedra', 'papel', 'tesoura']
    selecao_do_computador = random.choice(opcoes_do_jogo)
    selecao_do_usuario = opcoes_do_jogo[int(input('Escolha entre pedra, papel ou tesoura: \n 1. pedra \n 2. papel \n 3. tesoura \n'))-1]
    print(f'O computador escolheu {selecao_do_computador}.')
    print(f'O usuário escolheu {selecao_do_usuario}.')

    if selecao_do_usuario == selecao_do_computador:
        print('Empate!')
    elif selecao_do_usuario == 'pedra' and selecao_do_computador == 'tesoura':
        print('Você ganhou!')
    elif selecao_do_usuario == 'papel' and selecao_do_computador == 'pedra':
        print('Você ganhou!')
    elif selecao_do_usuario == 'tesoura' and selecao_do_computador == 'papel':
        print('Você ganhou!')
    else:
        print('Você perdeu!')
    input('Pressione ENTER para jogar novamente...')
    jokenpo()

jokenpo()