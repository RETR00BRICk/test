num1 = float(input("Перше число: "))
num2 = float(input("Друге число: "))
operation = input("Введіть потрібну дію: + | - | * | / | залишок | степінь ")
result = "Некоректно введена операція"
match operation:
    case "+": result = num1 + num2
    case "-": result = num1-num2
    case "*": result = num1*num2
    case "/": result = num1/num2
    case "залишок": result = num1%num2
    case "степінь": result = num1**num2
print(f">{result}")