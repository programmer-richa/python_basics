#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd

# Step 1: Creating a dictionary
section_A = {
        "1": {"Roll No": 1 ,"Name":"Rohan","Computer":100},
        "2": {"Roll No": 2 ,"Name":"Aryan","Computer":80},
        "3": {"Roll No": 3 ,"Name":"Mehak","Computer":50},
        "4": {"Roll No": 4 ,"Name":"Raghav","Computer":85},
        "5": {"Roll No": 5 ,"Name":"Priyanka","Computer":90},
}

# Test data type and data of a dictionary
print("-"*100,"\n","-"*100)
print("Type of section_A",type(section_A))
print("Value stored in section_A")
print(section_A)

print("-"*100,"\n","-"*100)


# Step 2: Create a datarframe of section_A
df_A=pd.DataFrame(section_A)

print("Type of df_A",type(df_A))
print("Value stored in df_A")
df_A


# In[ ]:





# In[ ]:




