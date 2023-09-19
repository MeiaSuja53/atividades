def replace_vogais(texto):
    return texto.replace ('a' , '*').replace ('A', '*').replace('e', '*').replace('E', '*').replace('i', '*').replace('I', '*').replace('o', '*').replace ('O', '*').replace('u','*').replace('U', '*')
print (replace_vogais(input('Digite uma palavra: ')))