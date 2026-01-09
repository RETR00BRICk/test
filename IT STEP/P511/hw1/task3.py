salary = float(input("Зарплата за місяць: "))
credit_pay = float(input("Сума щомісячного платежу за кредитом у банку: "))
need_pay = float(input("Заборгованість за комунальні послуги: "))
print(f"Залишається: {salary - credit_pay - need_pay}")