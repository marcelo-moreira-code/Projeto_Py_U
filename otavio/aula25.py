# Interpolação básica de strings

"""
s - string
d e i   - int
f - float
x e x - hexadecimal(ABCDEF012356789)
"""

nome = "Ana"
preco = 195.85
variavel = "%s, o preço é R$%.2f" % (nome, preco)
print(variavel)