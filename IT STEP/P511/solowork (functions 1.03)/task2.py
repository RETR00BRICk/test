def print_even_numbers(start : int, end : int):
    if start > end:
        start, end = end, start
    
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i)


print_even_numbers(2, 10)