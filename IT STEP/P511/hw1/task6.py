price_for_one_day = float(input("Вартість за 1 день: "))
days = int(input("Кількість днів: "))
pledge = float(input("Застава: "))
total_rent_money = price_for_one_day*days+pledge
remaining_money = total_rent_money - pledge
money_for_one_day = remaining_money/days
print("Користувачу потрібно сплатити за аренду: " + str(remaining_money))
print("Кожень день потрібно сплачувати: " + str(money_for_one_day))
