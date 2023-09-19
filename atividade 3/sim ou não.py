import random

def pergunta():
  return random.choice(["certa resposta, maroee", "lamentavel", "pode ser"])

def main():
  question = input("Digite uma pergunta: ")
  perg = pergunta()
  print(f"A resposta é: {perg}")

if __name__ == "__main__":
  main()