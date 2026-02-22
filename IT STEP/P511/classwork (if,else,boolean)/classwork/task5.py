num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
operation = input("Введіть потрібну операцію (+ | - | * | average): ")
result = "Вибраної операції не існує"
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "*":
    result = num1 * num2
elif operation == "average":
    result = (num1 + num2)/2

print(">" + str(result))
