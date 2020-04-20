# Creating a tuple from range
odd = tuple( i for i in range(1,10,2))
print("Type of odd", type(odd))
print("Value of odd", odd)
print("Accessing values of tuple", odd)
for i in odd:
    print(i)
