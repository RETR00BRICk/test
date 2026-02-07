num = int(input("Трьохзначне число: "))
if num > 999 or num < 100:
    print("Невірно введене число!")
else:
    lastdigit = num%10
    firstdigit = num//100
    seconddigit = (num%100)//10
    if lastdigit == firstdigit and firstdigit == seconddigit:
        print("всі цифри однакові")
    else:
        print("цифри різні")
