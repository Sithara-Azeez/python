b=int(input("Enter a number"))
try:
    c = 10 / b
    print(c)
    print("Try completed")
except ZeroDivisionError:
    print("Can't divided by zero")
    b = int(input("Enter a number other than zero"))
    c = 10 / b
    print(c)

print("Program completed")
