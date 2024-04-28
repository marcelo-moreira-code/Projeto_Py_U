nome = 'Ana'
sobrenome = 'Beatriz'
idade = 25
ano_nascimento = 1998
maior_de_idade = (2023-(ano_nascimento)) >= 18
altura_metros = 1.65
idade = 2023 - ano_nascimento


print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de Nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)

print(f'{nome} {sobrenome} , nasceu em {ano_nascimento}, portanto possui {idade} anos de idade e uma altura de {altura_metros} m.')