import math

try:
    value = float(input("Enter number "))
    if value < 0:
        raise Exception("Can't get sqrt of negative number")
    result = math.sqrt(value)
    print(f"Sqrt = {result}")
except ValueError:
    print("Not number")
except Exception as e:
    print(f"ERROR!: {e}")
finally:
    print("Operation ended")