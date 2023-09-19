def nome_do_usuario():
    nome = input("Digite seu nome: ").title()
    nome_usuario = nome.split()[0]
    sobrenome_usuario = nome.split()[1]
    print(f"Nome do: {nome.lower()}")
    print(f"Quantidade de letras: {len(nome)}")

nome_do_usuario()