# Concatenating  2 ranges
from itertools import chain
# creating 2 range variables
range1 = range(5)
range2 = range(0,11)
print(len(range2))
print(range2.count(1))
print(dir(range))
# Using chain method
print("Concatenating range1 and range2")


chain_of_two = chain(range1, range2)

print("Type of chain_of_two", type(chain_of_two))
print("Value of chain_of_two", chain_of_two)

for elem in chain_of_two:
    print("Type of elem in chain", type(elem),end='  ')
    print("Value of elem in chain", elem)
