text = input("Введіть текст: ")
reserved_words = ["python", "itstep", "c++"] 
words = text.split() #разбиваем строку на массив слов
result = []
for w in words:
    word = w.replace(",", "")
    word = word.replace(":", "") #убираем знаки припинания иначе не будет совпадения с выбраными словами
    if word.lower() in reserved_words: #мы тут проверяем текущее слово на соответсвие к базе слов
        result.append(w.upper())
    else:
        result.append(w) #если не совпало, то добавляем слово без изменений

print(" ".join(result)) #join помгает преобразовать массив в строку. Ну он склеивает элементы через в данном сулчае пробел