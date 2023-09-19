def contar_letras(texto):
  return len(texto)


texto = input("Digite um texto qualquer: ")
letras = contar_letras(texto)
print(f"O texto possui {letras} letras.")