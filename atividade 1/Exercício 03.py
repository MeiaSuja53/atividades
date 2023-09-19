def contador_letra():
  nome = input("Qual o seu nome completo? ")
  contador = 0
  for letra in nome.lower():
    if letra == "a":
      contador += 1
  print(contador)

contador_letra()