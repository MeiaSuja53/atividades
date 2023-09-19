def contador_de_letras():
  palavra = input("Digite uma palavra: ")
  contador = 0
  for letra in palavra:
    contador += 1
  print(contador)

contador_de_letras()