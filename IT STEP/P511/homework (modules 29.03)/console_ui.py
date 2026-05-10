def draw_header(title):
    width = 40
    print("=" * width)
    print(title.center(width))
    print("=" * width)

def draw_menu(options_list):
    for index, option in enumerate(options_list, start=1):
        print(f"[ {index} ] {option}")

def draw_warning(message):
    content = f"!!! {message} !!!"
    border = "!" * len(content)
    print(border)
    print(content)
    print(border)