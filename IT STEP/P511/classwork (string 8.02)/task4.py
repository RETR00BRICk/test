text = input("enter text> ")
start = input("enter start sybol> ")
end = input("enter end sybol> ")
if len(start) > 1 or len(end) > 1 or len(text) < 2:
    print("incorrect input")
else:
    cursor = 0
    start_index = 0
    while cursor < len(text):
        if text[cursor] == start:
            start_index = cursor
            cursor += 1
            break
        cursor += 1
    else:
        print("start sybol wasn't found")
        exit() #если первый символ не найден мы завершаем программу

    while cursor < len(text): #мы начинаем искать конечный символ с места, где был найден начальный
        if text[cursor] == end:
            break
        cursor += 1
    else:
        print("end sybol wasn't found")
        exit()

    print(text[start_index:cursor+1])