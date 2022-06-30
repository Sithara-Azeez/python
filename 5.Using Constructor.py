class Noor:
    year = 2022

    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place

    def add_age(self):
        self.age = self.age + 1

    def relocate(self, place):
        self.place = place

    def display(self):
        print("Year: " + str(Noor.year))
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Place: " + self.place)

    @classmethod
    def add_year(cls):
        cls.year = cls.year + 1

    @staticmethod
    def welcome():
        print("Welcome to NOOR")


Noor.welcome()
x = Noor("Sithara", 23, "Thalassery")
y = Noor("Nidha", 18, "Thalassery")

x.display()
y.display()

print("--------------------")
Noor.add_year()

x.add_age()
y.add_age()

x.display()
y.display()

print("--------------------")
Noor.add_year()

x.add_age()
y.add_age()
x.relocate("Dubai")
y.relocate("Chennai")
x.display()
y.display()
