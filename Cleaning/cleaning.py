import pandas as pd 
import numpy as np
df = pd.read_csv("car_cleaned_.csv")
missing = df.isna()
number_missing = missing.sum()
number_col=14

for i in range(len(df["Model"])):
    if(not(df["Model"][i]  ==  df["Model"][i])):
        if(df["Model"][i-1]  == df["Model"][i-1]):
            if(df["Make"][i-1] == df["Make"][i]):
                df["Model"][i]=df["Model"][i-1]	  
            if(i<(len(df["Model"])-1) and (df["Model"][i+1]  ==  df["Model"][i+1])):
              if(df["Make"][i+1] == df["Make"][i]):
                df["Model"][i]=df["Model"][i+1]
categorical=['Make','Engine Fuel Type','Transmission Type','Driven_Wheels','Vehicle Style']
for j in categorical:
      for i in range(len(df[j])):
        if(not(df[j][i]  ==  df[j][i])):
            if(df[j][i-1]  == df[j][i-1]):
                if(df["Model"][i-1] == df["Model"][i]):
                    df[j][i]=df[j][i-1]
                  
        if(i<(len(df[j])-1) and (df[j][i+1]  ==  df[j][i+1])):
            if(df["Model"][i+1] == df["Model"][i]):
                df[j][i]=df[j][i+1]


df['Vehicle Size'].fillna(method='bfill', inplace=True)

# c=0
categorical.append('Vehicle Size')

numerical=['Year','Engine HP','Engine Cylinders','Number of Doors'	,'highway MPG',	'city mpg',	'Popularity']

for i in numerical:
    df[i].fillna(round(int(df[i].mean()),1),inplace=True)
for i in categorical:
    df=df[df[i] == df[i]]

df.to_csv('car_cleaned.csv')   




