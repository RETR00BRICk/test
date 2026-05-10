numbers_input = input("Enter integers separated by spaces: ")
numbers = [int(x) for x in numbers_input.split()]

unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(f"List with unique elements: {unique_numbers}")