import random
import string

base_name = input("Enter your base name: ")

digital_num = random.randint(100, 9999)
variant1 = f"{base_name}{digital_num}"

separators = ["_", ".", "-"]
sep = random.choice(separators)
random_letters = "".join(random.choices(string.ascii_lowercase, k=3))
variant2 = f"{base_name}{sep}{random_letters}"

prefixes = ["Pro", "Super", "Ultra"]
prefix = random.choice(prefixes)
capital_name = base_name.capitalize()
random_digits = "".join(random.choices(string.digits, k=2))

elite_parts = list(capital_name + random_digits)
random.shuffle(elite_parts)
variant3 = prefix + "".join(elite_parts)

print("Generated nicknames:")
print(f"Variant 1: {variant1}")
print(f"Variant 2: {variant2}")
print(f"Variant 3: {variant3}")