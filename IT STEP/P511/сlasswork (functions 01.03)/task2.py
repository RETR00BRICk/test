def print_odd_numbers(start : int, end : int):
    for num in range(start, end + 1):
        print(f"{num} " if num%2 != 0 else "", end = "") #коротка запись условия, чтобы не городить внешние if else. f-строка для того чтобы сделать отступ

start = int(input("Введіть початок >>"))
end = int(input("Введіть кінець >>"))
print_odd_numbers(start,end)