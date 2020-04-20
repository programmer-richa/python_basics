# Creating tuple from value
coordinates = ((1,2),(3,4),(5,6),(7,8),(9,10))
print("Type of coordinates", type(coordinates))
print("Value of coordinates", coordinates)
# Looping over a nested tuple
for x,y in coordinates:
    print("Unpacked tuple values are:", x,"and",y)

# Looping over a nested tuple
for coordinate in coordinates:
    print("Type of coordinate", type(coordinate))
    print("Tuple Entry:",coordinate)

