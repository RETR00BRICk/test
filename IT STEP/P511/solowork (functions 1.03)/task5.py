def is_palindrome(number : int):
    number_str = str(abs(number))
    number_reversed = str()
    for char in number_str:
        number_reversed = char + number_reversed

    return number_reversed == number_str

print(is_palindrome(123321))
print(is_palindrome(123456654321))