import pandas as pd 
import numpy as np
# df = pd.read_csv("../Initial/cardataset.csv") 
df = pd.read_csv("car_cleaned_.csv")
missing = df.isna()
number_missing = missing.sum()
number_col=14
c=0
# for i in df[j]:
#       if(not(i==i)):
#             c+=1
            
print(c,"len=",len(df))
for i in range(len(df["Model"])):
    if(not(df["Model"][i]  ==  df["Model"][i])):
        if(df["Model"][i-1]  == df["Model"][i-1]):
            if(df["Make"][i-1] == df["Make"][i]):
                df["Model"][i]=df["Model"][i-1]	  
            if(i<(len(df["Model"])-1) and (df["Model"][i+1]  ==  df["Model"][i+1])):
              if(df["Make"][i+1] == df["Make"][i]):
                df["Model"][i]=df["Model"][i+1]
# For vehicle size , Run code again replacing vehicel size with other categorical coloumn names,same in differnt files and open the recently saved file
categorical=['Make','Engine Fuel Type','Transmission Type','Driven_Wheels','Vehicle Style']
# for j in categorical:
#       for i in range(len(df[j])):
#         if(not(df[j][i]  ==  df[j][i])):
#             if(df[j][i-1]  == df[j][i-1]):
#                 if(df["Model"][i-1] == df["Model"][i]):
#                     df[j][i]=df[j][i-1]
                  
#         if(i<(len(df[j])-1) and (df[j][i+1]  ==  df[j][i+1])):
#             if(df["Model"][i+1] == df["Model"][i]):
#                 df[j][i]=df[j][i+1]


df['Vehicle Size'].fillna(method='bfill', inplace=True)

# c=0
categorical.append('Vehicle Size')
# for i in range(len(df)):
#     if(not(df[categorical][i]==df[categorical][i])):
#         c+=1
# print("as",c)
numerical=['Year','Engine HP','Engine Cylinders','Number of Doors'	,'highway MPG',	'city mpg',	'Popularity']

for i in numerical:
    df[i].fillna(round(int(df[i].mean()),1),inplace=True)
for i in categorical:
    df=df[df[i] == df[i]]

# missing = df.isna()
# number_missing = missing.sum()
# print(number_missing)
# number_col=14
# mis=sum(number_missing)/(len(df)*number_col)
# print("Total ratio of missing values=",mis)
# print("percent of missing values=",mis*100)

df.to_csv('car_cleaned.csv')   




