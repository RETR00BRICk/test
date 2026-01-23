number = int(input("Введіть чотирьохзначне число: "))

if number > 9999 or number < 1000:
    print("Помилка! Введіть корректне значення")
else:
    num123 = number//10
    num12 = number//100
    num1 = number//1000

    num4 = number%10
    num3 = num123%10
    num2 = num12%10

    summ = num1 + num2 + num3 + num4
    print(f"Сума чисел = {summ}")
    if summ%2 == 0:
        print("Сума чисел парна")
    else:
        print("Сума чисел непарна")