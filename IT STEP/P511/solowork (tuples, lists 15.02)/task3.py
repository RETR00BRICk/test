numbers_input = input("Enter numbers separated by spaces: ")
numbers = [float(x) for x in numbers_input.split()]

positive_sum = 0
for num in numbers:
    if num > 0:
        positive_sum += num

print(f"Sum of positive numbers: {positive_sum}")