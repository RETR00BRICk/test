numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index: "))
    if index < 0: 
        raise IndexError
    print(f"Element with index {index}: {numbers[index]}")
except ValueError:
    print("invalid index. not an int number")
except IndexError:
    print("index outside the range")
finally:
    print("operation ended")