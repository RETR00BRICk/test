text = input("ENTER TEXT >>>> ")
words = text.split() #разбиваем строку на массив слов
words_reversed = reversed(words)
print(" ".join(words_reversed))