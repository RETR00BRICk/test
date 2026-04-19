numbers = input("Введіть список числел, наприклад 1 2 8 8 6 1 3 2 >>>")
numbers = numbers.split() #эта команда переводит строку в массив, элементы которого разъеденяются пробелами
num_set = set()
for number in numbers:
    num_set.add(int(number))
print(num_set)