# FIND SUM OF THE RANGE GIVEN BY USER
r = int(input("Enter a range you want to add"))
sum = 0
for i in range(1, r + 1):
    sum = sum + i
print(sum)
print("-----------------------------")

# Find Factorial of a range
factorial = 1
for i in range(1, r + 1):
    factorial = factorial * i
print(factorial)
