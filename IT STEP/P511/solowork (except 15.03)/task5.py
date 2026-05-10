data = input("Enter name, price, quantity with comma ")

try:
    parts = data.split(",")
    name = parts[0].strip()
    price = float(parts[1].strip())
    quantity = int(parts[2].strip())
    print(f"Name: {name}, Price: {price}, Count: {quantity}")
except IndexError:
    print("Incorrect input")
except ValueError:
    print("Incorrect values")
finally:
    print("operation ended")