print("-----------------------------------------")
print("      Simple Calculator      ")
print("-----------------------------------------")

operators=input("Enter operators (+. -, *, /): ")

num1=float(input("Enter first number: "))
num2=float(input("Enter Second number: "))

if operators=="+":
    result = num1+num2
    print(f"{num1} + {num2} = {result}")
elif operators == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operators == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operators == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator is Entered")