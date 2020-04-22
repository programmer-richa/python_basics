#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Step 1: Creating a dictionary
section_A = {
        "Roll No" : [1, 2, 3, 4, 5],
        "Name" : ["Rohan", "Aryan", "Mehak", "Raghav", "Priyanka"],
        "Computer" : [100, 95, 85, 50, 80],
}


# Step 2: Create a datarframe of section_A
df_A=pd.DataFrame(section_A)

# Step 3: Drop a Row in df_A
df_A=df_A.drop(df_A.index[2:4])

print("Type of df_A",type(df_A))
print("Value stored in df_A")
df_A


# In[ ]:




