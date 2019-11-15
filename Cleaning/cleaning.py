import pandas as pd 
import numpy as np
df = pd.read_csv("../Initial/cardataset.csv") 
missing = df.isna()
number_missing = missing.sum()
number_col=14

print(not(df["Model"][2]  ==  df["Model"][2]))
print(df["Model"][3]  ==  df["Model"][3])

c=0
# For vehicle size , Run code again replacing vehicel size with other categorical coloumn names,same in differnt files and open the recently saved file
categorical=['Make','Model','Engine Fuel Type','Transmission Type','Driven_Wheels','Vehicle Size','Vehicle Style']
for j in categorical:
  for i in df[j]:
      if(not(i==i)):
          c+=1
  print(c,"len=",len(df))

  for i in range(len(df[j])):
      if(not(df[j][i]  ==  df[j][i])):
        
          if(df[j][i-1]  == df[j][i-1]):
              if(df["Model"][i-1] == df["Model"][i]):
                  df[j][i]=df[j][i-1]
                  
          if(i<(len(df[j])-1) and (df[j][i+1]  ==  df[j][i+1])):
              if(df["Model"][i+1] == df["Model"][i]):
                  df[j][i]=df[j][i+1]
                
categorical=['Vehicle Style']
for i in categorical:
  df[j].fillna(method='bfill', inplace=True)

c=0

for i in range(len(df["Vehicle Size"])):
    if(not(df["Vehicle Size"][i]==df["Vehicle Size"][i])):
        c+=1
print("as",c)
numerical=['Year','Engine HP','Engine Cylinders',	'Number of Doors'	,'highway MPG',	'city mpg',	'Popularity']

for i in numerical:
  df[i].fillna(round(int(df[i].mean()),1),inplace=True)

missing = df.isna()
number_missing = missing.sum()
number_col=14
mis=sum(number_missing)/(len(df)*number_col)
print("Total ratio of missing values=",mis)
print("percent of missing values=",mis*100)

df.to_csv('car_cleaned.csv')   




