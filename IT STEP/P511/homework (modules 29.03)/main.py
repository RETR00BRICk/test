import console_ui

if __name__ == "__main__":
    console_ui.draw_header("СУПЕР ГРА 2024")

    menu_items = ["Нова гра", "Завантажити збереження", "Вихід"]
    console_ui.draw_menu(menu_items)

    print("=" * 40)
    
    choice = input("Введіть ваш вибір: ")
    if choice not in menu_items: console_ui.draw_warning("Не існує такого вибору!")