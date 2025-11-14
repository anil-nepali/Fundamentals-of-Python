print("-----------------------------------------")
print("      Currency Convertor      ")
print("-----------------------------------------")

amount = float(input("Enter the Amount :"))
currency = input("Enter the currency (IND, USD, JPY, KRW, AUD):")

if currency.upper() == "IND":
    result = round(amount*1.6,2)
    print(f"The Indian ₹{amount} is Nepali {result} rupees. ")
elif currency.upper() == "USD":
    result = round(amount* 141.87,2)
    print(f"The American ${amount} is Nepali {result} rupees.")
elif currency.upper() == "JPY":
    result = round(amount * 0.92,2)
    print(f"The Japneese ¥{amount} is Nepali {result} rupees.")
elif currency.upper() == "KRW":
    result = round(amount * 0.0966,2 )
    print(f"The Korean ₩{amount} is Nepali {result} rupees.")
elif currency.upper() == "AUD":
    result = round(amount * 93.05,2)
    print(f"The Austrillian AU${amount} is Nepali {result} rupees.")

else:
    print("Invalid currency entered.")
print("-----------------------------------------")
    

