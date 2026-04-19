text = input("Enter text>>> ")
end_sentence = ".?!"
sentence_count = 1 #учитываем предложение в конце текста
if len(text) < 1:
    print ("incorrect input")
else:
    for char_index in range(len(text)-1): #-1 сделано, чтобы мы не учитывали точку в конце текста. Так как текст может заканчиваться и без неё
        if text[char_index] in end_sentence:
            sentence_count += 1

print(sentence_count)
