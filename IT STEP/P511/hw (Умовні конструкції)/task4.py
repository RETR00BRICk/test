meters = float(input("Кількість метрів: "))
print("В які одиниці ви хочете перевести значення? 1 - в милі, дюйми, ярди (на вибір)")
print("2 - перевести одразу в усі три одиниці (милі, дюйми та ярди)")
print("3 - перевести в кілометри та сантиметри")
choise = int(input("Введіть ваш вибір: 1, 2 чи 3 >>"))
result = "некорекно введене значення"
if choise == 1:
    choiseFirst = int(input("в які саме одиниці: 1 - милі, 2 - дюйми, 3 - ярди >>"))
    if choiseFirst == 1:
        result = 0.00062137*meters
    elif choiseFirst == 2:
        result = 39.3701*meters
    elif choiseFirst == 3: 
        result = 1.0936*meters
elif choise == 2:
    result = f"милі: {0.00062137*meters}    дюйми: {39.3701*meters}    ярди: {1.0936*meters}"
elif choise == 3:
    result = f"кілометри: {meters/1000}    сантиметри: {100*meters}"
print(">" + str(result))