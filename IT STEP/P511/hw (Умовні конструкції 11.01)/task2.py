num1 = float(input("Перше число: "))
num2 = float(input("Друге число: "))
num3 = float(input("Третє число: "))
choise = input("Введіть дію: min | max | average: ")
result = "Некоректно введена операція"
if choise == "min":
    result = min(num1, num2, num3)
elif choise == "max":
    result = max(num1, num2, num3)
elif choise == "average":
    result = (num1 + num2 + num3)/3

print(result)