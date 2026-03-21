num = float(input("Введіть число:"))
power = int(input("Введіть степінь:"))
result = 1
for i in range(abs(power)):
    result *= num

if power < 0: 
    if result == 0:
        result = "Ділення на нуль неможливе"
    else: result = 1/result
print(result)