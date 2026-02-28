numbers = input("Введіть список чисел, наприклад 1,3,4,3,6,8,1 ")
numbers = numbers.split() #эта команда разделяет строку в массив через пробелы. То есть 1 2 3 будет ['1','2','3']
num_set = set()
for number in numbers:
    num_set.add(int(number))
print(num_set)