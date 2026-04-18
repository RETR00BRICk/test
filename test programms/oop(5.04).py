class Animal:
    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} of type {self.type} made sound {self.sound}")

    def __str__(self):
        return f'Name: {self.name}\nType: {self.type}\nSound: {self.sound}'
    
animal1 = Animal("Buddy", "dog", "Wof!")
animal2 = Animal("Bob", "parrot", "sqwawk!")
animal1.make_sound()
animal2.make_sound()

print(animal1, animal2, sep = "\n")