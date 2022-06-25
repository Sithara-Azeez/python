#Length of the string
a = "Sithara Anaz"
print(len(a))
print("-------------------------------------")

#using index
a="hello welcome to this world"
print(a[0:7])
print(a[:11])
print(a[-8:-1])
print(a[:-5])

print("-------------------------------------")

#Looping through string
for x in "sithara":
    print(x)
print("-------------------------------------")

#checking a char in a string

txt = "you are pro in Django"
print("pro" in txt)           # we will use 'in' keyword
print("-------------------------------------")

#USING IF pro in txt
if "pro" in txt:
    print("pro is Present")
print("-------------------------------------")

#CHECK IF NOT
print("free" not in txt)           # USING 'not in'
print("-------------------------------------")

if "expense" not in txt:
    print("you are right,expense is not there")
print("-------------------------------------")

''' SLICING STRING''' #using start index and end index
a = "Hello World"
print(a[:7])
print("-------------------------------------")

'''MODIFY STRING''' #Python has a set of built-in-methods
print(a.upper())
print(a.lower())
b = " Hello World "
print(b.strip())        #remove WHITESPACE
print(a.replace("H","A"))

print(a.split("W"))     #returns a list with seperation
print("-------------------------------------")

'''CONCATENATE STRING'''
a = "hello"
b = "world"
c = a + " " + b
print(c)
print("-------------------------------------")

'''ESCAPE SEQUENCE'''
t = "why you called me \"intelligent\" "
print(t)
t = 'it\'s alright use \\(backslash)'
print(t)
