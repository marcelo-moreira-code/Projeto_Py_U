# Operadores Lógicos 
# and          not
# or  
# None

"""
Em resumo
Valores truthy são valores que são avaliados como True em um contexto booleano.
Valores falsy são valores que são avaliados como False em um contexto booleano.
Valores falsy incluem sequências vazias (listas, tuplas, strings, dicionários, sets), zero em qualquer tipo numérico, None e False.
valores truthy incluem sequências não vazias, números (exceto 0 em qualquer tipo numérico) e, basicamente, qualquer valor que não for falsy.
Eles podem ser usados para tornar seu código mais conciso.
"""

# falsy

entrada = input("[E]ntrada ou [S]air: ").upper()
print(entrada)

senha_digitada = input("Senha: ")


senha_permitida = "123456"

if entrada == "E" and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print("Sair")    

# Tabela verdade / Avaliação de curto circuito

"""
if 0 and 1:
    print("True and 1")"""


"""# Expression 5 < 3
if 5 < 3:
    print("True")
else:
    print("F")

# Output
False"""


"""
A Função integrada bool()  
Você pode verificar se um valor é truthy ou falsy com a função integrada bool().



De acordo com a  documentação do Python, essa função:

Retorna um valor booleano, ou seja, True ou False. x (o argumento) é convertido usando o procedimento padrão de teste de verdade.
"""

a = 0

if a:
    print(a)

"""
🔸 Valores Falsy 
Sequências e coleções:

Listas vazias []
Tuplas vazias ()
Dicionários vazios {}
Sets vazios set()
Strings vazias ""
Ranges vazios range(0)
Números

Zero de qualquer tipo numérico.
Inteiro: 0
De ponto flutuante: 0.0
Complexo: 0j
Constantes

None
"""

"""
bool(5)
True
bool(0)
False
bool([])
False
bool({5, 5})
True
bool(-5)
True
bool(0.0)
False
bool(None)
False
bool(1)
True
bool(range(0))
False
bool(set())
False
bool({5, 6, 2, 5})
True
"""