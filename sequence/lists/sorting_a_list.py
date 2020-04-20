# creating a list

names = ["Richa","Sonia","Ria","Ana","Aahna"]
print("Type of names", type(names))
print("Value of names", names)
print("Sorting elements of a list")
names.sort()
print("Type of names", type(names))
print("Value of names", names)

# creating a list

students = [["Richa","Sonia","Ria","Ana"],"Aahna"]
print("Type of students", type(students))
print("Value of students", students)
print("Sorting elements of an inner list")
# sorts a list in ascending order
students[0].sort()
# to sort in decending order
students[0].reverse()
print("Type of students", type(students))

print("Value of students", students)
