class First:
    def display(self):
        print("first")

class Second:
    def display(self):
        print("Second")

class Third(First,Second):
    def display_third(self):
        print("Third")

x = Third()
x.display()
print(Third.__mro__)