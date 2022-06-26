#Function in python

def hello():
    print("hello, it's a function")
hello()
print("-------------------------------------")

#Argument passing to method

def hey(name,age):
    print("My name is "+name+" "+"and am "+str(age))
value = "Sithara Anaz"
hey(value,23)
print("--------------------------------------------")

#ARBITARY ELEMENT -- multiple parameters passing to a method
def hai(*values):
    print("first:"+values[0]+" second:"+values[1])

hai("sithu","nidha")