def remover_gogais(texto):
  gogais = "aeiouAEIOU"
  sem_gogais = ""
  for letra in texto:
    if letra not in gogais:
      sem_gogais += letra
  return sem_gogais


texto = input("Digite um algo: ")
sem_gogais = remover_gogais(texto)
print(sem_gogais)