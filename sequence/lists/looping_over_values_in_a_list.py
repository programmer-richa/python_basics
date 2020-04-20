# creating List from  values
whole_numbers = [0,1,2,3,4,5,6,7,8,9]
print("Type of whole_numbers", type(whole_numbers))
print("Value of whole_numbers", whole_numbers)
print("Looping over whole_numbers list:")
for value in whole_numbers:
    print(value)

# Creating String from List of values
str = ",".join(str(i) for i in whole_numbers)
print("Values stored in whole_numbers are ",str)
