#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Step 1: Create first dictionary
section_A = {
        "Roll No" : [1, 2, 3, 4, 5],
        "Name" : ["Rohan", "Aryan", "Mehak", "Raghav", "Priyanka"],
        "Computer" : [100, 95, 85, 50, 80],
}

# Step 2: Create first data frame of section_A
df_A=pd.DataFrame(section_A)

# Step 3: Create second dictionary
section_B = {
        "Roll No" : [6, 7, 8, 9, 10],
        "Name" : ["Rashmi", "Richa", "Sandeep", "Jaspreet", "Bhavika"],
        "Computer" : [75, 65, 95, 100, 55],
}

# Step 4: Create second data frame
df_B=pd.DataFrame(section_B)

# Step 5: Concate data frames

df = pd.concat([df_A,df_B],ignore_index=1)

# Step 6:  Sort data frame
df.sort_values(by=['Computer'],inplace=True,  ascending=False)

# Step 7: Selecting bottom 3 students
bottom = df.tail(3)
print("Type of top",type(bottom))
print("Value stored in bottom")
bottom


# In[ ]:




