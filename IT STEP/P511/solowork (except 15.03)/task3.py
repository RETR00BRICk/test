sales_input = input("Enter numbers with space between: ")

try:
    sales_list = [float(sale) for sale in sales_input.split()]
    total = sum(sales_list)
    print(f"All sum of sales: {total}")
except ValueError:
    print("Not numbers!")
finally:
    print("Operation ended")