# Concatenation of List
# creating list of first five positive integers
postive = [1,2,3,4,5]
# creating list of first five negative integers
negative = [-1,-2,-3,-4,-5]

# Joining 2 lists
all =postive + negative
# By using the following statement positive list will have values stored in negative lists as well
# positive.extend(negative)
# Joining 2 lists using slice
partial =postive + negative[1:3]

print("Type of postive", type(postive))
print("Value of postive", postive)

print("Type of negative", type(negative))
print("Value of negative", negative)

print("Type of all", type(all))
print("Value of all", all)

print("Type of partial", type(partial))
print("Value of partial", partial)

