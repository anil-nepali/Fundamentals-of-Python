print("-------------------------------------------------------------")
print("      Temperature Convertor      ")
print("-------------------------------------------------------------")


unit = input("Is this temperature is in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the Temperatrue:"))
if unit.upper()=="C":
    temp = round((9*temp)/5 + 32,2)
    print(f"The temperature in fahrenheit is :{temp}°F")
elif unit.upper()=="F":
    temp = round((temp-32)*5/9,2)
    print(f"The temperature in celsius is :{temp}°C")
else:
    print(f"{unit} is an Invalid unit of a measurement")

print("-------------------------------------------------------------")