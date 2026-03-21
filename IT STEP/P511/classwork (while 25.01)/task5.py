num1 = int(input("Введіть початок діапазону>>> "))
num2 = int(input("Введіть кінець діапазону>>> "))
start = min(num1,num2) #чтобы пользователь мог вводить диапазон в любом порядке
end = max(num1,num2)

product = 1 #первоначальное значение. Ноль бы не подошел, потому что все произведение в таком случае оставалось бы нулями
for num in range(start, end+1):
    if num % 4 == 0 and num % 6 != 0:
        product *= num

if product != 1:
    print(product)
else:
    print("Таких чисел нема")