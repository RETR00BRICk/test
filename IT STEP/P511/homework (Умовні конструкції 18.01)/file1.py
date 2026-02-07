num = float(input("Введіть число"))
power = int(input("Введіть степінь числа"))
if power < 0 or power > 7:
    print("Помилка, введіть значення від 0 до 7")
else:
    result = pow(num, power)
    print(result)