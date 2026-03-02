num1 = int(input("Введіть початок діапазону>>> "))
num2 = int(input("Введіть кінець діапазону>>> "))
start = min(num1,num2) #чтобы пользователь мог вводить диапазон в любом порядке
end = max(num1,num2)

step = int(input("введіть шаг>> "))
reverse = (input("Вивести діапазон в зворотньому порядку? (True/False)>> "))

if reverse == "False":
    counter = start
    while counter < end:
        counter += step
        print(counter)
else:
    counter = end
    while counter > start:
        counter -= step
        print(counter)