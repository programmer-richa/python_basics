#
# Method 1: Deleting value using remove() function
#


# creating List from  values
whole_numbers = [0,1,2,3,4,5,6,7,8,9]
print("Type of whole_numbers", type(whole_numbers))
print("Value of whole_numbers", whole_numbers)
print("Removing 9 from the whole_numbers list")
# '9' is removed
whole_numbers.remove(9)

# Updated whole_numbers List
print('Updated whole_numbers list: ', whole_numbers)




# creating List from  values
numbers = [1,2,3,4,5,2,3,4,2]
print("Type of numbers", type(numbers))
print("Value of numbers", numbers)
print("Removing 2 from the numbers list having multiple  occurances of value 2")
#  only first occurance of '2' is removed
numbers.remove(2)

# Updated whole_numbers List
print('Updated numbers list: ', numbers)


# removing all occurances of 2
print("Removing all occurances of 2 using while loop")
while 2 in numbers:
    numbers.remove(2)
print('Updated numbers list: ', numbers)



#
#  Method 2: Deleting element using del statement
#
print("Removing values from index 1 and 2 using del statement")
del numbers[1:3]
print('Updated numbers list: ', numbers)

#
#  Method 3: Deleting element using pop method
#
print("Removing element at index 2 from the list using pop method")
object_removed = numbers.pop(2)
print('Updated numbers list: ', numbers)
