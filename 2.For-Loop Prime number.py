n = int(input("Enter a number to find prime number or not"))
flag = 0
for i in range(2, n):
    if n % 2 == 0:
        flag = 1
        break
if flag == 0:
    print("Number is Prime number")
else:
    print("number is Not Prime number")
