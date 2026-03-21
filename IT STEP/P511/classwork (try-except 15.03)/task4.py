available_amount = 1000
try:
    target_ammount = int(input("Введіть бажану сумму:"))
    if target_ammount > available_amount: raise Exception("Недостатньо коштів на балансі")
except ValueError:
    print("Некорректно введене значення")
except Exception as ex:
    print(ex.args[0])
finally:
    print("")