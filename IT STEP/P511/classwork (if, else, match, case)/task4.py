number = int(input("Введіть шестизначне число: "))
if number < 100000 or number > 999999:
    print("Помилка! Введіть корректне значення")
else:
    first_digits = number//1000
    last_digits = number%1000

    firstsum = first_digits%10 + (first_digits//10)%10 + (first_digits//100)
    lastsum = last_digits%10 + (last_digits//10)%10 + (last_digits//100)

    if firstsum == lastsum:
        print("Щасливе число!")
    else:
        print("Число нещасливе!")
