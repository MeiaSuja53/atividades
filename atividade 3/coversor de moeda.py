def converter(moeda_origem, moeda_destino, valor, taxa):

  if moeda_origem == moeda_destino:
    return valor

  return valor * taxa


def main():

  moeda_origem = input("qual moeda de origem? ")
  moeda_destino = input("qual moeda de destino? ")
  taxa = float(input("qual taxa de câmbio? "))

  valor = float(input("Digite o valor a ser convertido: "))

  valor_convertido = converter(moeda_origem, moeda_destino, valor, taxa)

  print(f"O valor convertido é {valor_convertido} {moeda_destino}.")


  main()