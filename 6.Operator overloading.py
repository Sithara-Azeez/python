class Sample:
    def set_name(self,name):
        self.name = name

    def __add__(self, other):
        name = self.name +" "+other.name
        return name


first = Sample()
second = Sample()
first.set_name("Sithara")
second.set_name("Anaz")
full_name = first + second
print(full_name)