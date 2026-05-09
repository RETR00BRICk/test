dictionary = {
    "apple": "яблуко",
    "book": "книга",
    "ocean": "океан",
    "sun": "сонце",
    "cloud": "хмара"
}

word = input("Введіть англійське слово: ").lower()

if word in dictionary:
    print(dictionary[word])
else:
    print("Слово не знайдено")