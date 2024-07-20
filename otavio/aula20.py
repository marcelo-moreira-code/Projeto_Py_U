# if / elif / else

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
False
Valores falsos foram a razão pela qual não houve saída em nosso exemplo inicial, quando o valor de a era zero.

O valor 0 é falsy. Portanto, a condição if será False e o condicional não será executado neste exemplo:

a = 0
if a:
    print(a)

# Sem resultado

"""


"""
🔹 Valores Truthy:
Segundo a documentação do Python:

Por padrão, um objeto é considerado verdadeiro.
Valores Truthy incluem:

Sequências ou coleções não vazias (listas, tuplas, strings, dicionários, sets).
Valores numéricos que não são zero.
True
Esse é o motivo pelo qual o valor de a foi impresso em nosso exemplo inicial, pois seu valor foi 5 (um valor truthy):

a = 5

if a:
    print(a)
    
# Resultado
 5


"""