people_count = int(input("Скільки людей було в ресторані: "))
order_price = float(input("Вартість заказу загалом: "))
tip_price = order_price*0.15
total_price = tip_price + order_price
price_for_one_guest = total_price/people_count

print(f"Кожна людина повинна сплатити: {price_for_one_guest}")