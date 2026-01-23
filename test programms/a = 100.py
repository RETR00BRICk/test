a = 100
b = 50

if a > b: print("a быльше b")
10 + 11 #бынарный оператор
num = -10
-num #унарний оператор

age = 17
#canvote = age >= 18 ? True : False
print("a > b") if a > b else (print("a < b") if a < b else print("a дорівнює b") )

login = input("Ведіь ваш логін")
display_name = login if login else 'Гість'
print(f'Привіт, {display_name}')


age = 18
if age < 18:
    pass # TODO: Implement underage logic later
else:
    print("Full access granted")

day = int(input("День тижня"))
match day:
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("Saturday")
    case 7: print("Sunday")
    case _: print("Некорректний номер дня!!1")
    
months = int(input("Номер місяця"))

match months:
    case 12 | 1 | 2: print("Зима")
    case 3 | 4 | 5: print("Весна")
    case 6 | 7 | 8: print("Літо")
    case 9 | 10 | 11: print("Осінь")
    case _: print("Wrong number")
day = int(input("номер дня"))

match day:
    case 1 | 2 | 3 | 4 | 5 if months == 12:
        print("Будній день в грудні")
    case 1 | 2 | 3 | 4 | 5 if months == 1:
        print("Будній день в січні")
    case 6 | 7 if months == 12:
        print("Вихідний день в грудні")
    case 6 | 7 if months == 1:
        print("Вихідний день в січні")
