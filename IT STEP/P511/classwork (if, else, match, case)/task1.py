grade = int(input("Введіть бал: "))
if 90 <= grade <= 100:
    print("Відмінно")
elif 70 <= grade <= 89:
    print("Добре")
elif 50 <= grade <= 69:
    print("Задовільно")
elif 0 <= grade <= 49:
    print("Незадовільно")
else:
    print("Неправильно введений бал")