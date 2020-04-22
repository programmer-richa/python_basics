#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd

# Step 1: Creating a dictionary
section = {
        0: {"Roll No": 1 ,"Name":"Rohan","Computer":100,"Maths":90},
        1: {"Roll No": 2 ,"Name":"Aryan","Computer":80,"Maths":85},
        2: {"Roll No": 3 ,"Name":"Mehak","Computer":50,"Maths":57},
        3: {"Roll No": 4 ,"Name":"Raghav","Computer":85,"Maths":65},
        4: {"Roll No": 5 ,"Name":"Priyanka","Computer":90,"Maths":80},
}


# Step 2: Create a datarframe of section
df=pd.DataFrame(section)

# Step 3: Transpose dataframe
df =df.transpose()


# Step 4: Get all rows

rows = df.iterrows()

# using Lists
totals =[]
for index,row in rows:
    totals.insert(index,row["Computer"]+row["Maths"])

# using dictionary
# totals ={}
# for index,row in rows:
#     totals[index]=(row["Computer"]+row["Maths"])
# df["Total"]=totals.values()  
    
df["Total"]=totals
print("Type of df",type(df))
print("Value stored in df")
df


# In[ ]:




