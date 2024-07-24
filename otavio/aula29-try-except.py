"""
try - tenta executar o código

except - ocorreu algum erro ao tentar executar


erros são exceções
"""


"""
print(12354)
print("Oi")
print(float("a"))"""

"""num = float(input("Digite um número para ter o seu dobro: "))
print(f"O dobro do número {num} é {num * 2}")
"""

numero_str = input("Vou dobrar o número que você digitar: ")

try:
    print("STR: ",numero_str)
    numero_float = float(numero_str)
    print("FLOAT: ",numero_float)
    print(f"O dobro do {numero_str} é {numero_float * 2:.2f}")
    ...
except:
    print("Isso não é um número")
    ...