# Creating variables of type int
x = 10
y = 15
print("Type of x", type(x))
print("Value of x", x)
print("Type of y", type(y))
print("Value of y", y)

# Packing a tuple
coordinate = (x,y)
print("Type of coordinate", type(coordinate))
print("Value of coordinate", coordinate)

# Creating a list
numbers = [1,2,3,4]
print("Type of numbers", type(numbers))
print("Value of numbers", numbers)

# Creating a string
name = "Richa"
print("Type of name", type(name))
print("Value of name", name)

# Adding all elements created above in a tuple
tuple_obj = (x, y, coordinate, numbers, name)
print("Type of tuple_obj", type(tuple_obj))
print("Value of tuple_obj", tuple_obj)
print((('-'*20)+"\n")*2,"Looping over tuple")
# Looping over a heterogeneous tuple
for element in tuple_obj:
    if type(element) is int or type(element) is str:
        print("Type of element", type(element))
        print("Tuple element:",element)
    elif type(element) is tuple or type(element) is list:
            values = (',').join(str(value) for value in element)
            print("Type of element", type(element))
            print("Values:",values)
