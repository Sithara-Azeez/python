# hey() calling GLOBAL VARIABLE
values = 10


def hey():
    print(values)


hey()
print(values)
print("------------------------------")


# hello() calling LOCAL VARIABLE

def hello():
    values = 30
    print(values)


hello()
print(values)
print("------------------------------")

# we can't access global variable to local--
'''def hai():
    values = values + 1
    print(values)'''


# instead of values we have to assign another variable name--
def hai():
    s = values + 1
    print(s)
hai()