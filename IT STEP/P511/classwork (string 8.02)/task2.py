text = input("ENTER TEXT>>> ").replace(" ", "") #чтобы убрать пробелы между словами
half_len = len(text)//2
first_half = text[0:half_len]
second_half = text[-half_len:]
print("Слово є паліндромом" if first_half == second_half[::-1] else "слово не є паліндромом")