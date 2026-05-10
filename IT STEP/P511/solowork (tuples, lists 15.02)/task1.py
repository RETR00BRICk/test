numbers_input = input("Enter integers separated by spaces: ")
numbers = [int(x) for x in numbers_input.split()]

total_sum = sum(numbers)
average = total_sum / len(numbers)

print(f"Sum: {total_sum}")
print(f"Average {average}")