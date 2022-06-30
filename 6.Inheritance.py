class BaseClass:
    def display(self):
        print("helloo")


class SubClass(BaseClass):
    def welcome(self):
        print("Welcome")


x = BaseClass()
y = SubClass()
x.display()
y.welcome()
y.display()
