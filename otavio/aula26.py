# f strings 
# 
# .<número de dígitos>f
# (Caractere)(><`^)(quantidade)
# > - esquerda
# < - direita
# ^ - centro
# Sinal - + ou -
# 
# Ex.: 0>-100, .1f
# Coversion flags - !r !s !a
# 
# #


variavel = "ABCDE"
print(f"{variavel}")
print(f"{variavel: >15}")
print(f"{variavel: <15}")
print(f"{variavel: ^15}")
