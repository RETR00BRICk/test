payment = float(input("Введіть зарплату"))
years = float(input("Введіть стаж роботи"))
premium = 0.0
if years < 1:
    print("Премія не передбачена")
elif 1 <= years <= 3:
    premium = 0.05
elif 3 < years <= 5:
    premium = 0.1
else:
    premium = 0.15

if years >= 1:
    print(f"Премія {premium*100}% від зарплати")
    print(f"Премія = {premium*payment}")