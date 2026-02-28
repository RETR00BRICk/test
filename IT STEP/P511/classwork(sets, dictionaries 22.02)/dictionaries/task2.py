text = input("Enter text>>>")
text = text.split() # чтобы преобразовать весь текс в список
words = dict()
for word in text:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

for word in words:
    print(f"{word} - {words[word]}")