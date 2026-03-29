def to_power(number: float, power: int):
    if power == 1:
        return number
    elif power == 0:
        return 1
    elif power > 1:
        return number * to_power(number, power-1)
    elif power < 0: #чтобы отрицательные степени тоже работали
        return 1 / (number * to_power(number, abs(power)-1)) #прикол в abs - это модуль. То есть единицу делит на результат только в ПЕРВОМ вызове функции

number = float(input("Enter number >>>"))
power = int(input("Enter power >>>"))
print(to_power(number, power))