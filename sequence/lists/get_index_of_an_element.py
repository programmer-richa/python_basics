# creating List from  values
whole_numbers = [0,1,2,3,4,5,6,7,8,9]
print("Type of whole_numbers", type(whole_numbers))
print("Value of whole_numbers", whole_numbers)
try:
    index_of_3 = whole_numbers.index(3)
    print("Type of index_of_3", type(index_of_3))
    print("Value of index_of_3", index_of_3)
except:
    print("3 does not exist in the list")

try:
    index_of_30 = whole_numbers.index(30)
    print("Type of index_of_30", type(index_of_30))
    print("Value of index_of_30", index_of_30)
except:
    print("30 does not exist in the list")




