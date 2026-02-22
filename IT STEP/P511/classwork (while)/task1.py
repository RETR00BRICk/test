num1 = int(input("Введіть перше число"))
num2 = int(input("Введіть друге число"))
numbers = ""
currentNumber = 0
if num1 < num2:
    currentNumber = num1
else:
    currentNumber = num2

while currentNumber <= num2:    
    numbers += str(currentNumber) + " "
    currentNumber += 1

print(numbers)
