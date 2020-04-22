#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# Step 1: Creating a dictionary
section_A_Computer = {
        "1": {"Roll No": 1 ,"Name":"Rohan","Computer":100},
        "2": {"Roll No": 2 ,"Name":"Aryan","Computer":80},
        "3": {"Roll No": 3 ,"Name":"Mehak","Computer":50},
        "4": {"Roll No": 4 ,"Name":"Raghav","Computer":85},
        "5": {"Roll No": 5 ,"Name":"Priyanka","Computer":90},
}


# Step 2: Create a datarframe of section_A_Computer
df_A_Computer=pd.DataFrame(section_A_Computer)

# Step 3: Transpose dataframe
df_A_Computer =df_A_Computer.transpose()

# Step 4: Creating a dictionary
section_A_Maths = {
        "1": {"Maths":90},
        "2": {"Maths":85},
        "3": {"Maths":57},
        "4": {"Maths":65},
        "5": {"Maths":80},
}


# Step 5: Create a datarframe of section_A_Maths
df_A_Maths=pd.DataFrame(section_A_Maths)

# Step 6: Transpose dataframe
df_A_Maths =df_A_Maths.transpose()

df_A = pd.merge(df_A_Computer, df_A_Maths, left_index = True , right_index = True)

print("Type of df_A",type(df_A))
print("Value stored in df_A")
df_A


# In[ ]:




