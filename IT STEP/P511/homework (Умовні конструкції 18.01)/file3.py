discount = 0
price = 0
null = "Нічого"
regular_client = input("Ви постійний клієнт: true / false") == "true"
print("Закуски: Салат, Суп")
first_choice = input("Оберіть: Салат, Суп, Нічого")
print("Основні десерти: Курка, Риба")
second_choice = input("Оберіть: Курка, Риба, Нічого")
print("Десерти: Морозиво, Фрукти")
third_choice = input("Оберіть: Морозиво, Фрукти, Нічого")


match first_choice:
    case "Салат": price += 5
    case "Суп": price += 7
match second_choice:
    case "Курка": price += 10
    case "Риба": price += 12
match third_choice:
    case "Морозиво": price += 3
    case "Фрукти": price += 4

if first_choice == "Суп" and second_choice == "Риба" and third_choice != null:
    price -= 2
if second_choice == "Курка" and third_choice == "Морозиво":
    print("Вам надано безкоштовний чай у подарунок")

if first_choice != null and second_choice != null and third_choice != null:
    discount += 0.1
    if price > 20:
        discount = 0.15
if regular_client:
    discount += 0.05



total = price - (price*discount)

print(f"Загальна вартість: {total}")
