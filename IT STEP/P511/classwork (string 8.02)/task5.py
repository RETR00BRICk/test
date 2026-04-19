text = input("enter text to check: ")
chars_to_check = input("enter sybols to remove: ")

words = text.split() #преобразовываем текст в массив слов
result_words = []
for word in words:
    add_word = True
    for char in word:
        if char in chars_to_check:
            add_word = False        
            break
    if add_word: result_words.append(word)


result_text = " ".join(result_words)

print(result_text)