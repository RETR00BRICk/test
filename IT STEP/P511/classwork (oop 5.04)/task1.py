class Student:
    def __init__(self, name, surname, age, grade_list : list):
        self.name = name
        self.surname = surname
        self.age = age
        self.grade_list = grade_list

    def __str__(self):
        return f"{self.name} {self.surname}, {self.age} y.o., grades:{self.grade_list}"

    def print_grades(self):
        print(f"Список оцінок студента {self.name} {self.surname}:")
        for i in range(len(self.grade_list)):
            print(f"№{i+1} - {self.grade_list[i]}")

    def add_grade(self, grade : int):
        self.grade_list.append(grade)

class Car:
    def __init__(self, brand, model, speed, year):
        self.brand = brand
        self.model = model
        self.speed = speed
        self.year = year
    
    def __str__(self):
        return f"{self.brand}, {self.model}, {self.speed}, {self.year}"

    def print_info(self):
        print(f"This {self.year} {self.brand} {self.model} reaches speed up to {self.speed} km/h")

car = Car("VAZ","2107",120,1982)
student = Student("terry", "davidson", 19, [11,10,8,10,5,7])
while True:
    print("===class testing menu===")
    print("write 'q' to quit the programm.")
    class_choice = input("Which class do you want to test: Car or Student >>>")
    match class_choice.lower():
        case "car":
            action_choise = input("Which function to call: 'str' or 'print info' >>>")
            match action_choise.lower():
                case "str": print(car)
                case "print info": car.print_info()
                case _: print("function doesn't exist")
        case "student":
            action_choise = input("Which function to call: 'str', 'print grades' or 'add grade' >>>")
            match action_choise.lower():
                case "str": print(student)
                case "print grades": student.print_grades()
                case "add grade":
                    grade = int(input("Print grade to add >>>"))
                    student.add_grade(grade)
                case _: print("function doesn't exist")
        case "q": break
        case _: print("needed class does not exist")
