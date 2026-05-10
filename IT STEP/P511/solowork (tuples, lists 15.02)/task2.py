numbers_input = input("Enter integers separated by spaces:  ")
numbers = [int(x) for x in numbers_input.split()]

target = int(input("Enter the number to count: "))
count = numbers.count(target)

print(f"number appears {count} times")