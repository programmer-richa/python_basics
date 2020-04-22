#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd

# Step 1: Creating a dictionary
section_A = {
        "Roll No" : [1, 2, 3, 4, 5],
        "Name" : ["Rohan", "Aryan", "Mehak", "Raghav", "Priyanka"],
        "Computer" : [100, 95, 85, 50, 80],
}

# Test data type and data of a dictionary
print("-"*100,"\n","-"*100)
print("Type of section_A",type(section_A))
print("Value stored in section_A")
print(section_A)

print("-"*100,"\n","-"*100)


# Step 2: Create a datarframe of section_A
df_A=pd.DataFrame(section_A)

# Step 3: a new Column in df_A
df_A["Maths"] =maths

# Using DataFrame.insert() to add a column 
# df_A.insert(2, "Maths", maths, True) 
print("Type of df_A",type(df_A))
print("Value stored in df_A")
df_A


# In[ ]:




