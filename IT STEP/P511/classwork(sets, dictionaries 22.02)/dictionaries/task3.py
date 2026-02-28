rates = {"USD": 40.2, "EUR": 42.5, "PLN": 9.6}
money = float(input("Введіть сумму у гривнях >> "))
money_type = input("Введіть валюту: USD, EUR, PLN >> ")
if money_type not in rates:
    print("Такої валюти не існує")
else:
    print(f"Ось {money} гривень у {money_type}>> {rates[money_type]*money}")