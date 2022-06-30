# Method  Overriding
class BaseClass:
    def __init__(self):
        print("Base init")

    def set_name(self, name):
        self.name = name
        print("Base method called")


class SubClass(BaseClass):
    def __init__(self):
        print("Sub init")

    def set_name(self, name):
        self.name = name
        print("Sub method called")

    def display_name(self):
        print("Name: " + self.name)


x = SubClass()
x.set_name("Sithara Anaz")
x.display_name()