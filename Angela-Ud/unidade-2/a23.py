# 1st input : enter height in meters
height = float(input("Enter your height in meters: "))
# 2nd input: enter weight in kilograms
weight = float(input("Enter weight in kilograms: "))

imc = weight/(height)**2

print(f"Your imc is: {imc:.2f}")