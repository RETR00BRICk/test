try:
    dollars = int(input("Dollars amount: "))
    rate = float(input("Dollars to euro exchange rate: "))
    if rate == 0: raise(Exception("exchange rate can't be equal to zero!"))
    print(f"euros= {dollars*rate}")
except ValueError:
    print("Incorrect value input")
except Exception as ex:
    print(ex.args[0])
finally:
    print("Operation ended")
