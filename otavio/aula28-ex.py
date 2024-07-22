"""
Exercício

Peça para ao usuário para digitar seu nome e sua idade
se o nome e idade forem digitados:
Exiba:
    Seu nome é 
    Seu nome invertido é 
    Seu nome contém ou não espaços
    Seu nome tem letras
    A primeira letra do seu nome é 
    A última letra do seu nome é 
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."


"""

nome = (input("Digite seu nome: "))
idade = (input("Digite sua idade: "))

if nome and idade:    
    print("Analisando o seu nome...")
    print(f"O seu é {nome}")
    print(f"Seu nome invertido fica {nome[::-1]}")
    print(f"Seu nome possue {len(nome)} letras")
    print(f"Seu nome contém {nome.count(" ")} espaços")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[-1]}") 
else:
    print("Desculpe, você deixou campos vazios.")    