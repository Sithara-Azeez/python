class BaseClass:
    def set_name(self, name):
        self.name = name


class SubClass(BaseClass):
    def display_name(self):
        print("Name: " + self.name)


x = SubClass()
x.set_name("Sithara Anaz")
x.display_name()