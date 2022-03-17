import sys
import time

print("""𝕮𝖆𝖑𝖈𝖚𝖑𝖆𝖙𝖔𝖗""")


print("Operations: Add, Subtract, Multiply, Divide")
select = input("Select operations: ")


if select == "Add":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(num1, "+", num2, "=", num1+num2)


elif select == "Subtract":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(num1, "-", num2, "=", num1-num2)
    

elif select == "Multiply":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(num1, "*", num2, "=", num1*num2)


elif select == "Divide":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(num1, "/", num2, "=", num1/num2)

else:
    print("The selection", select, "is invalid, Please choose Add/Subtract/Multiply/Divide")
    sys.exit