# creating List from  values
whole_numbers = [1,2,3,4,5,6,7,8,9,10]
print("Type of whole_numbers", type(whole_numbers))
print("Value of whole_numbers", whole_numbers)
starting_point = 0
ending_point = 4

first_four_elements_list =whole_numbers[starting_point:ending_point]
print("Type of selected_list", type(first_four_elements_list))
print("Value of selected_list", first_four_elements_list)


starting_point_from_end = -5
ending_point_from_end = -1

last_four_elements_list =whole_numbers[starting_point_from_end:ending_point_from_end]
print("Type of last_four_elements_list", type(last_four_elements_list))
print("Value of last_four_elements_list", last_four_elements_list)

# The following statement will return first element in the list
print("Selecting 1st elemet in the list", whole_numbers[-0])
print("Selecting 1st elemet in the list", whole_numbers[-0:1])
