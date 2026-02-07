grade = int(input("Введіть оцінку від 1 до 5: "))
match grade:
    case 1: print("дуже погано")
    case 2: print("погано")
    case 3: print("задовільно")
    case 4: print("добре")
    case 5: print("відмінно")
    case _: print("некорректне значення")
