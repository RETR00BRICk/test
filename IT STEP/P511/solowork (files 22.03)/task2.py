try:
    with open("log.txt", "r") as file:
        text = file.read().lower()
        words = text.split()

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1


    sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)

    top_10 = sorted_words[:10]

    with open("word_stats.txt", "w") as out_file:
        for word, count in top_10:
            out_file.write(f"{word}: {count}\n")
    
    print("Top 10 words saved to word_stats.txt")
except FileNotFoundError:
    print("Error: log.txt not found.")