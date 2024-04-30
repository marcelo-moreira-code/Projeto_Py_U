"""
Welcome to the tip calculator!
What was the total bill?
how much tip would you like  ti give?
"""
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill in $?\n"))
tip = float(input("How much tip would you like to give? 10, 12 or 15%? \n"))
people = int(input("how many people ti split the bill? \n"))
print(f"Each person should pay: {(total_bill*(tip/100 + 1)) / people:.2f}")