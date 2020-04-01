import keyword
#print keywords list
print(keyword.kwlist)
# initializing strings for testing
s = "for"
s1 = "richa"
# checking which are keywords
if keyword.iskeyword(s):
    print(s + " is a python keyword")
else:
    print(s + " is not a python keyword")

if keyword.iskeyword(s1):
    print(s1 + " is a python keyword")
else:
    print(s1 + " is not a python keyword")
