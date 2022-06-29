class MySampleClass:
    def hello(self):
        print("Hello")


x = MySampleClass()
x.hello()
''' Or we can call like this
# MySampleClass.hello(x) '''
print("-------------------------------------")

#Argument passing to a function

class MySampleClass:
    def hello(self,n):
        print("Hello "+n)


x = MySampleClass()
name = "sithara"
x.hello(name)
print("-------------------------------------")

#To store variable in class

class MySampleClass:
    def hello(self,n):
        self.name = n

    def print_name(self):
        print(self.name)


x = MySampleClass()
y = MySampleClass()
name = "Sithara Anaz"
x.hello(name)
y.hello("nitu choudhary")

x.print_name()
y.print_name()
print("-------------------------------------")

