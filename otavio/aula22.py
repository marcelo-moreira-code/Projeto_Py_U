# or
# 
"""
entrada = input("[E]ntrada ou [S]air: ").upper()
print(entrada)

senha_digitada = input("Senha: ")


senha_permitida = "123456"

if entrada == "E" and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print("Sair")   """

senha = input("Senha: ")  or "Sem senha"
print(senha)