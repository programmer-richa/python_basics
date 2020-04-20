# list containing objects of different data type
#creating empty list
data =list()
data.append("Ram")
data.append(32)
data.append(3.14)

print("Type of data", type(data))
print("Value of data", data)

# Looping over List
for elem in data:
    print("Type of elem:", type(elem),", Value of elem:", elem)
    print()
