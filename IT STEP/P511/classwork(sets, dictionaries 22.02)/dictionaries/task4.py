translations = {
    "яблуко" : "apple",
    "ківі" : "kiwi",
    "ананас" : "pineapple",
    "помело" : "pamelo",
    "гарбуз" : "pumpkin",
    "кавун" : "watermelon",
    "диня" : "melon",
    "банан" : "banana"
}
while True:
    word = input("Введіть слово, яке бажаєте перекласти, або введіть 'q' щоб вийти >> ")
    if word == 'q': break
    if word in translations:
      print(f"#{word}# на англійській буде #{translations[word]}#")
    else:
       print(f"Слово #{word}# не знайдено!")