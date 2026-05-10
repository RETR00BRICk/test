try:
    num1 = float(input("First num:  "))
    num2 = float(input("Second num:  "))
    result = num1 / num2
    print(result)
except ValueError:
    print("Not a number")
except ZeroDivisionError:
    print("zero divison")
finally:
    print("operation ended")