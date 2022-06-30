# Method  Overriding
class BaseClass:
    def __init__(self):
        print("Base init")

    def set_name(self, name):
        self.name = name
        print("Base method called")


class SubClass(BaseClass):
    def __init__(self):
        # BaseClass.__init__(self)          we can call __init__(constructor) like this also, we should pass self obj
        super().__init__()              # standard way to call Base class
        print("Sub init")

    def set_name(self, name):
        # self.name = name
        super().set_name(name)             # by using super class, we can call the method
        print("Sub method called")

    def display_name(self):
        print("Name: " + self.name)


x = SubClass()
x.set_name("Sithara Anaz")
x.display_name()