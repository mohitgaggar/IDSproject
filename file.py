import pandas as pd 
import numpy as np

df = pd.read_csv("newcar6.csv") 

missing = df.isna()
number_missing = missing.sum()
number_col=14
c=0
for i in range(len(df["Model"])):
    if(not(df["Model"][i]==df["Model"][i])):
        print(i)
        c+=1

print("Model nans",c,"len=",len(df))
c=0
for i in range(len(df["Make"])):
    if(not(df["Make"][i]==df["Make"][i])):
        print(i)
        c+=1
c=0
print("make nans",c,"len=",len(df))
for i in range(len(df["Vehicle Size"])):
    if(not(df["Vehicle Size"][i]==df["Vehicle Size"][i])):
        print(i)
        c+=1


print("vehicle",c)

