num1 = int(input("Enter 2 numbers"))
num2 = int(input())
choice = int(input("1-Addittion\n2-Substraction\n3-Multiplication\n4-Division"))
if choice == 1:
    result = num1 + num2
    print(result)
elif choice == 2:
    result = num1 - num2
    print(result)
elif choice == 3:
    result = num1 * num2
    print(result)
elif choice == 4:
    result = num1 / num2
    print(result)
else:
    print("Invalid option")
