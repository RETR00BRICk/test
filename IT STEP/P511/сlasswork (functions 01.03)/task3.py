def draw_line(length : int, symbol : str, direction : str):
    if direction == "горизонтальна":
        ending = ""
    elif direction == "вертикальна":
        ending = "\n"
    else:
        print("неккоретне значення напрямку")
        return
    print(f"{symbol}{ending}"*lengh)

lengh = int(input("введіть довжину >>"))
symbol = input("Введіть символ >>")
direction = input("введіть напрямок (вертикальна/горизонтальна) >>")
draw_line(lengh,symbol,direction)