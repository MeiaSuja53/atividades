import random

def gerar_senha(tamanho):

  caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"
  senha = ""
  for i in range(tamanho):
    senha += random.choice(caracteres)
  return senha


def main():
 
  tamanho = int(input("Digite o tamanho da senha: "))

  senha = gerar_senha(tamanho)

  print(f"A senha gerada é: {senha}")


if __name__ == "__main__":
  main()