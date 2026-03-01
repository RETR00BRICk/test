
choise = input("Введіть літеру фігури, яку хочете побачити: е ж з и к а б в г д>>")
length = int(input("Введіть розмір фігури>>"))
match choise:
    case "е":
        for counter in range(1,length//2): #это не ИИ писал, честно. Я просто на бумажке считал сколько и где отступов нужно
            print("#" * counter, end = "")
            print("."*(length - counter*2), end = "")
            print("#" * counter)
        for counter in range(length//2, 0, -1): #делаем тоже самое, только вверх ногами, инвертируя счетчик
            print("#" * counter, end = "")
            print("."*(length - counter*2), end = "")
            print("#" * counter)
    case "ж":
        for counter in range(1,length//2 + 1): 
            print("#" * counter)
        for counter in range(length//2, 0, -1):
            print("#" * counter)
    case "з":
        for counter in range(1,length//2 + 1): 
            print("."*(length - counter), end = "")
            print("#" * counter)
        for counter in range(length//2, 0, -1): 
            print("."*(length - counter), end = "")
            print("#" * counter)
    case "и":
        for counter in range(length, 0, -1):
            print("#"*counter)
    case "к":
        for counter in range(1,length + 1): 
            print("."*(length - counter), end = "")
            print("#" * counter)
    case "а":
        for counter in range(length, 0, - 1): 
            print("."*(length - counter), end = "")
            print("#" * counter)
    case "б":
        for counter in range(1, length + 1):
            print("#"*counter)
    case "в":
        for counter in range(1,length//2+1): 
            print("." * counter, end = "")
            print("#"*(length - counter*2))
    case "г":
        for counter in range(length//2, 0, -1):
            print("." * counter, end = "")
            print("#"*(length - counter*2))
    case "д":
        for counter in range(1,length//2): 
            print("." * counter, end = "")
            print("#"*(length - counter*2), end = "")
            print("." * counter)
        for counter in range(length//2, 0, -1):
            print("." * counter, end = "")
            print("#"*(length - counter*2), end = "")
            print("." * counter)

