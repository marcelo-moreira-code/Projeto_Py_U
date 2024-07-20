num1 = float(input("Digite um número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O {num1} é maior que {num2}")
elif num2 > num1:
    print(f"O {num2} é maior que {num1}")
else:
    print(f"Os dois números possuem o mesmo valor {num1} = {num2}")        
