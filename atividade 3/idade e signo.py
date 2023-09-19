def idade_do_user(ano_de_nascimento):
  idade = 2023 - ano_de_nascimento
  return idade

def cal_signo(mes, dia):
  signos = {
    'aresto': (3, 21),
    'chifrudo': (4, 20),
    'gemilios': (5, 21),
    'cancerigino': (6, 21),
    'liaozim': (7, 23),
    'virgem?': (8, 23),
    'mudim': (9, 23),
    'espirpiao': (10, 23),
    'agitariano': (11, 22),
    'capricorno': (12, 22),
    'no armario': (1, 20),
    'pixes': (2, 19)
  }

  for signo, (mes_inicio, dia_inicio) in signos.items():
    if mes == mes_inicio and dia >= dia_inicio:
      return signo
    elif mes == mes_inicio + 1 and dia < dia_inicio:
      return signo

  return None

ano_de_nascimento = int(input('Digite o ano de nascimento: '))
idade = idade_do_user(ano_de_nascimento)
print(f'Nossa ta vei ehn já tem{idade} anos.')

mes = int(input('Digite o numero mês de nascimento: '))
dia = int(input('Digite o dia de nascimento: '))
signo = cal_signo(mes, dia)
print(f'Seu signo é {signo}.')