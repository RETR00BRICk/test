number = int(input("Введіть шестизначне число: "))
if number < 100000 or number > 999999:
    print("Помилка! Введіть корректне значення")
else:
    num12 = number//10000
    num34 = (number//100)%100
    num56 = number%100

    num1 = num12//10
    num2 = num12%10
    
    num5 = num56//10
    num6 = num56%10
   
    new_num = num6*100000 + num5*10000 + num34*100 + num2*10 + num1

    print(new_num)
    
    