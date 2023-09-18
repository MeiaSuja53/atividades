def login():
    nome = input ("Qual e o seu nome? ")
    sobrenome = input ("Qual o seu sobrenome? ")
    return nome [:3] + sobrenome[:3]
print(login())