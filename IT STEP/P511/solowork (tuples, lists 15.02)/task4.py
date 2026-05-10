numbers_input = input("Enter integers separated by spaces>>> ")
numbers = [int(x) for x in numbers_input.split()]

even_i = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_i.append(i)

print(f"Indices of even numbers: {even_i}")