import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        return self.radius**2 * math.pi
    def get_perimeter(self):
        return math.tau * self.radius #tau это 2*pi. То есть 2*pi*R = tau*R

class Triangle():
    def __init__(self, side1, side2, side3):
        self.sides = (side1, side2, side3)
    def get_area(self):
        s = self.sides
        if s[0] + s[1] <= s[2] or s[0] + s[2] <= s[1] or s[1] + s[2] <= s[0]:
            return 0
        p = (s[0] + s[1] + s[2]) / 2
        area = math.sqrt(p * (p - s[0]) * (p - s[1]) * (p - s[2]))
        return area
    def get_perimeter(self):
        return sum(self.sides)

class Rectangle():
    def __init__(self, side1, side2):
        self.sides = (side1, side2)
    def get_area(self):
        return self.sides[0] * self.sides[1]
    def get_perimeter(self):
        return 2*sum(self.sides)


while True:
    print("=== menu ===")
    print("1. circle")
    print("2. triangle")
    print("3. rect")
    print("print Q to exit")
    choice = input("CHOOSE>>> ")
    match choice:
        case "1":
            r = float(input("radius: "))
            shape = Circle(r)
        case "2":
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
            shape = Triangle(a, b, c)
            if shape.get_area() == 0:
                print("invalid traingle sides!")
                continue
        case "3":
            a = float(input("a: "))
            b = float(input("b: "))
            shape = Rectangle(a, b)
        case "Q":     
            break
        case _:
            print("invalid command")
            continue
    print("\n"*3)
    print(f"area: {shape.get_area()}")
    print(f"perimeter: {shape.get_perimeter()}")
