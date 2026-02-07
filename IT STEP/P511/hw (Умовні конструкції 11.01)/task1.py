num1 = float(input("Перше число: "))
num2 = float(input("Друге число: "))
num3 = float(input("Третє число: "))
choise = input("Введіть дію: + або * ")
result = "Некоректно введена операція"
if choise == "+":
    result = num1 + num2 + num3
elif choise == "*":
    result = num1 * num2 * num3


print(">" + str(result))
