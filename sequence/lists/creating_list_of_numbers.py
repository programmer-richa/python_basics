'''
Python offers a range of compound datatypes often referred to as sequences.
List is one of the most frequently used and very versatile datatype used in Python.

List is a collection which is ordered and changeable. Allows duplicate members.
'''
# creating List from  values
whole_numbers = [0,1,2,3,4,5,6,7,8,9,10]
print("Type of whole_numbers", type(whole_numbers))
print("Value of whole_numbers", whole_numbers)

# creating List from  range function
starting_point_of_range = 0
# stopping_point_of_range is excluded from the range
stopping_point_of_range = 11
# increment value in range by steps_of_range
steps_of_range = 1
range_list =[i for i in range(starting_point_of_range,stopping_point_of_range,steps_of_range)]
print("Type of range_list", type(range_list))
print("Value of range_list", range_list)



