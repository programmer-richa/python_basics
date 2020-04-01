# Arithmetic operators
a = 10
b = 3

add = a + b
sub = a - b
div = a / b
integral_div = a // b
mod = a % b

print("Arithmetic Operations On ", a, " & ", b, " are as follows: ")
print("_____________________________________________","\n")
print("Addition: ", add)
print("Subtraction: ", sub)
print("Division: ", div)
print("Integral Division: ", integral_div)
print("Modulus: ", mod)

# Relational operators
print("\nRelational Operations On ",a," & ",b," are as follows: ")
print("_____________________________________________","\n")
print("Greater than: ", a > b)
print("Less than: ", a < b)
print("Greater than equal to : ", a >= b)
print("Less than equal to : ", a <= b)
print("Is equal to : ", a == b)
print("Not equal to : ", a != b)
print("Modulus: ",mod)

# Logical operators
print("\nLogical Operations On ",a," & ",b," are as follows: ")
print("_____________________________________________","\n")
print("a>0 and a > b: ", a>0 and a > b)
print("a>0 or a < b: ", a>0 or a < b)
print("not(a >= b): ", not(a >= b))

# Bitwise operators
print("\nBitwise Operations On ",a," & ",b," are as follows: ")
print("_____________________________________________","\n")
print("a & b: ", a & b)
print("a | b: ", a | b)
print("~a: ", ~a)
print("a ^ b: ", a ^ b)
print("a >> b: ", a >> b)
print("a << b: ", a << b)

# Assignment operators
print("\nAssignment Operations On ",a," & ",b," are as follows: ")
print("_____________________________________________","\n")
a += 2
print("a += 2: ", a)
a -= 2
print("a -= 2: ", a)
a *= 2
print("a *= 2: ", a)
a /= 2
print("a /= 2: ", a)
a %= 2
print("a %= 2: ", a)
a //= 2
print("a //= 2: ", a)
a **= 2
print("Exponent , a **= 2: ", a)
a = 100
print("a = 1: ", a)
a &= 2
print("a &= 2: ", a)
a |= 2
print("a |= 2: ", a)
a ^= 2
print("a ^= 2: ", a)
a >>= 2
print("a >>= 2: ", a)
a <<= 2
print("a <<= 2: ", a)

# Special operators
print("\nSpecial Operations On ",a," & ",b," are as follows: ")
print("_____________________________________________","\n")
'''
Identity operators-
is and is not are the identity operators both are used to check if two values are located on the same part of the memory. 
Two variables that are equal does not imply that they are identical.
        is          True if the operands are identical 
        is not      True if the operands are not identical 
        
Membership operators-
in and not in are the membership operators; used to test whether a value or variable is in a sequence.
        in            True if value is found in the sequence
        not in        True if value is not found in the sequence
'''
# Examples of Identity operators
a1 = 3
b1 = 3
a2 = 'Richa'
b2 = 'Richa'
a3 = [1,2,3]
b3 = [1,2,3]
print(a1 is not b1)
print(a2 is b2)
# Output is False, since lists are mutable.
print(a3 is b3)

# Examples of Membership operator
x = 'I love Python'
y = {3: 'Ram', 4: 'Mohan'}

print("'o' in x: ", 'o' in x)
print("'python' not in x: ", 'python' not in x)
print("'Python' not in x: ", 'Python' not in x)
print("3 in y: ", 3 in y)
print("'Mohan' in y: ", 'Mohan' in y)
