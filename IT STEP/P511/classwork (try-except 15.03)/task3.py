try:
    rates = input("введіть список оцінок студентів через пробіл >>>")
    rates_list = rates.split()
    rates_int_list = list(map(int, rates_list))
    summ = sum(rates_int_list)
    average = summ/len(rates_int_list)
    print(average)
except ValueError:
    print("Некорректно введені оцінки!")
except ZeroDivisionError:
    print("Список оцінок порожній!")
finally:
    print("Завершення обчислень")