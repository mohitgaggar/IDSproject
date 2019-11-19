from sklearn import preprocessing
import pandas as pd 
import numpy as np
# load the Iris dataset
df = pd.read_csv("standardization/normalized_car.csv") 
# print(df.values.shape)
# separate the data and target attributes

c=0
numerical=['Year','Engine HP','Engine Cylinders',	'Number of Doors'	,'highway MPG',	'city mpg',	'Popularity']
print(df[numerical].mean())
print(df[numerical].describe())
print(df[numerical].var())
