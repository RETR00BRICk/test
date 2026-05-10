def sum_digits(n : int):
    n = abs(n)
    if n < 10:
        return n
    return (n % 10) + sum_digits(n // 10)

num = int(input("Enter number: "))
print(sum_digits(num))