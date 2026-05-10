def draw_square(side : int, symbol : str, filled : bool):
    for i in range(side):
        if filled:
            print(symbol * side)
        else:
            if i == 0 or i == side - 1:
                print(symbol * side)
            else:
                spaces = " " * (side - 2)
                print(symbol + spaces + symbol)

draw_square(5, "*", False)