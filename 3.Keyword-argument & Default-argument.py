# KEYWORD ARGUMENT - we can give arguments unordered by mentioning the keyword
def hello(name, age):
    print(name, age)
hello(age=23,name="Sithara Anaz")
print("-------------------------------")

#DEFAULT ARGUMENT - we can set default value to the function
def hey(name,place="kannur"):
    print(name,place)
hey("Sithara")
hey("Anaz")
hey("preeti","Delhi")
