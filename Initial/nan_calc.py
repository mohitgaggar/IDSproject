import pandas as pd 
import numpy as np

df = pd.read_csv("cardataset.csv") 

missing = df.isna()
number_missing = missing.sum()
number_col=14
# print("Total Percentage of missing values=",sum(number_missing)/(len(df)*number_col))
# print(df["Model"])
print(not(df["Model"][2]  ==  df["Model"][2]))
print(df["Model"][3]  ==  df["Model"][3])

c=0
for i in df["Model"]:
    if(not(i==i)):
        c+=1
print(c,"len=",len(df))

for i in range(len(df["Model"])):
    if(not(df["Model"][i]  ==  df["Model"][i])):
        # print(df["Model"][i],"HIHI")
        if(df["Model"][i-1]  ==  df["Model"][i-1]):
            if(df["Make"][i-1] == df["Make"][i]):
                df["Model"][i]=df["Model"][i-1]
                # print(df["Model"][i])
        if(i<(len(df["Model"])-1) and (df["Model"][i+1]  ==  df["Model"][i+1])):
            if(df["Make"][i+1] == df["Make"][i]):
                df["Model"][i]=df["Model"][i+1]
                # print(df["Model"][i])


        
# print(df["Model"])
c=0
l=[]
k=0
for i in range(len(df["Model"])):
    if(not(df["Model"][i]==df["Model"][i])):
        c+=1
        l.append(i)
print("as",l)
c=0
for i in l:
    print(df["Model"][i])
    df=df.drop(df.index[i-c])
    c=c+1
# for i in range(len(df["Model"])):
#     if(not(df["Model"][i]==df["Model"][i])):
#         c+=1
print("V",c)

df.to_csv('newcar1.csv')    
# df[df["Model"] !=df["Model"]]
# c=0
# for i in range(len(df["Model"])):
#     if(not(df["Model"][i]==df["Model"][i])):
#         print(i)
#         c+=1
# print("3",c,"len=",len(df))
#print(df.head())
# missing = df.isna()
# number_missing = missing.sum()
# number_col=14
# print("Total Percentage of missing values after",sum(number_missing)/(len(df)*number_col))

#number_percent=number_missing / len(df)
#print(number_percent)
#print("sum=",sum(number_percent)/len(number_percent))

