class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def speak(self):
        if self.species.lower() == 'dog':
            print("Woof!")
        elif self.species.lower() == 'cat':
            print("Meow!")
        else:
            print("I'm a silent creature!")

    def birthday(self):
        self.age += 1
        print(f"🎉Happy Birthday {self.name}!🎉")
        print(f"{self.name} is now {self.age} years old!")

    def showinfo(self):
        print(f"{self.name}\t{self.species}\t{self.age}")
