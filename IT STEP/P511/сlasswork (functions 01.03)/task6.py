def is_lucky_number(number):
    number = abs(number)
    number_str = str(number)
    if len(number_str) != 6:
        print("Error, number is not 6 digits long")
        return False

    digits = [int(d) for d in str(number)]
    first_half = digits[:3]
    second_half = digits[3:]
    return sum(first_half) == sum(second_half)

print(is_lucky_number(123420))
print(is_lucky_number(883991))