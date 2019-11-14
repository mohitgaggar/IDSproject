import pandas as pd 
import numpy as np
df = pd.read_csv("cat_cleared.csv") 
# missing = df.isna()
# number_missing = missing.sum()
# number_col=14

# print(not(df["Model"][2]  ==  df["Model"][2]))
# print(df["Model"][3]  ==  df["Model"][3])

# c=0

# for i in df["Vehicle Size"]:
#     if(not(i==i)):
#         c+=1
# print(c,"len=",len(df))

# for i in range(len(df["Vehicle Size"])):
#     if(not(df["Vehicle Size"][i]  ==  df["Vehicle Size"][i])):
       
#         if(df["Vehicle Size"][i-1]  ==  df["Vehicle Size"][i-1]):
#             if(df["Model"][i-1] == df["Model"][i]):
#                 df["Vehicle Size"][i]=df["Vehicle Size"][i-1]
                
#         if(i<(len(df["Vehicle Size"])-1) and (df["Vehicle Size"][i+1]  ==  df["Vehicle Size"][i+1])):
#             if(df["Model"][i+1] == df["Model"][i]):
#                 df["Vehicle Size"][i]=df["Vehicle Size"][i+1]
                
categorical=['Vehicle Style']
for i in categorical:
  df[i].fillna(method='bfill', inplace=True)

c=0

for i in range(len(df["Vehicle Size"])):
    if(not(df["Vehicle Size"][i]==df["Vehicle Size"][i])):
        c+=1
print("as",c)

# for i in range(len(df["Vehicle Size"])):
#     if(not(df["Vehicle Size"][i]==df["Vehicle Size"][i])):
#         c+=1

df.to_csv('newcar6.csv')   


