# creating list inside a list
#initializing empty list
numbers = []

#appending a list to numbers list
numbers.append([1,2,3])

#appending a list to numbers list
numbers.append([4,5,6])
numbers.append(7)
numbers.append(8)
print("Type of numbers", type(numbers))
print("Value of numbers", numbers)

# Looping over numbers List
for elem in numbers:
    elem_type =type(elem)
    if elem_type is list:
       values = ",".join(str(value) for value in elem)
       print("Type of elem:", type(elem),", Value of elem:", values)
    else:
        print("Type of elem:", type(elem),", Value of elem:", elem)
