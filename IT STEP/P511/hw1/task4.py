path = float(input("Довжина шляху: "))
price_for_gas = float(input("Вартість 1 літру бензину: "))
gas_waste = float(input("Витрата бензину на 100км: "))

gas_total = path*gas_waste
price_total = gas_total*price_for_gas

print("Вартість поїздки = "+ str(price_total))
