import pandas as pd 
import numpy as np

df = pd.read_csv("cardataset.csv") 
print(df.head())
missing = df.isna()
number_missing = missing.sum()
number_col=14
print("Total Percentage of missing values=",sum(number_missing)/(len(df)*number_col))

#number_percent=number_missing / len(df)
#print(number_percent)
#print("sum=",sum(number_percent)/len(number_percent))

