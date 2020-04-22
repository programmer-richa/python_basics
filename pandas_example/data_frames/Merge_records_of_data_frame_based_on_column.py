#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

# Step 1: Create first dictionary
section_A_Computer = {
        "Roll No" : [1, 2, 3, 4, 5],
        "Name" : ["Rohan", "Aryan", "Mehak", "Raghav", "Priyanka"],
        "Computer" : [100, 95, 85, 50, 80],
}

# Step 2: Create first data frame of section_A_Computer
df_A_Computer=pd.DataFrame(section_A_Computer)

# Step 3: Create second dictionary
section_A_Maths = {
        "Roll No" : [1, 2, 3, 4, 5],
        "Maths" : [75, 65, 95, 100, 55],
}

# Step 4: Create first data frame of section_A_Maths
df_A_Maths=pd.DataFrame(section_A_Maths)

# Step 5: Joining Records based on "Roll No"

df = pd.merge(df_A_Computer,df_A_Maths,on="Roll No")
print("Type of record",type(df))
print("Value stored in record")
df


# In[ ]:




