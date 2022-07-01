import datetime

#print DATE & TIME


print(datetime.datetime.now())

#print DATE
print(datetime.date.today())

#Formate date
now = datetime.datetime.now()
print(now.strftime("%d/%m/%Y"))

# To give a date
x = datetime.date(2022,12,31)
print(x)

# To check difference
x = datetime.date(1998,8,11)
y = datetime.date(2004,4,22)
dif = x-y
print(dif)
end = datetime.datetime.now()
print(end)
difference = now - end
print(difference)