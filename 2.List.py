values = ["Python", "Django", "C"]
print(values)
print("-------------------------------------")

# IF I WANT TO CHANGE THE VALUES
values[2] = "Java"
print(values)
print("---------------------------------")

# LENGTH OF THE LIST
print(len(values))
print("-------------------------------------")

# IF  WE WANT LAST VALUE FROM THE LIST
print(values[-2])
print("-------------------------------------")

# ADD ANOTHER LIST TO VALUES
values = values + ["C", "Ruby"]
print(values)
print("-------------------------------------")

# ADD ONE ITEM TO THE END OF THE LIST
values.append("23")
print(values)
print("-------------------------------------")

# Add ONE ITEM TO THE END FROM THE USER
values.append(input("Enter a value:"))
print(values)
