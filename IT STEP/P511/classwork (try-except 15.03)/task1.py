try:
    original_price = float(input("Початкова ціна: "))
    discount = float(input("Знижка: "))
    print(original_price - original_price*discount/100)
except ValueError:
    print("Incorrect input number!")