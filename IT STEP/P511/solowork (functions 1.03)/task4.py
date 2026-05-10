def count_digits(number : int) -> int:
    number_str = str(abs(number))
    return len(number_str)

result = count_digits(1234)
print(result)