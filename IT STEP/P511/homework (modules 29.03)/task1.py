import random as rd
import string as s

def get_variant_1(nickname : str):
    return nickname + str(rd.randint(100,9999))

def get_variant_2(nickname: str):
    symbols = filter(lambda symbol: symbol in "-._",s.punctuation)
    letters = rd.choices(s.ascii_lowercase, k = 3)
    print(letters)

nickname = input("Введіть ім'я>> ")
print(f"Перший варіант нікнейму: {get_variant_1(nickname)}")

get_variant_2("dd")