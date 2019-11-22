# Standardize the data attributes for the Iris dataset.
# from sklearn.datasets import load_iris
from sklearn import preprocessing
import pandas as pd 
import numpy as np
# load the Iris dataset
df = pd.read_csv("../Cleaning/car_cleaned.csv") 
numerical=['Year','Engine HP','Engine Cylinders',	'Number of Doors'	,'highway MPG',	'city mpg',	'Popularity','MSRP']
df[numerical] =preprocessing.MinMaxScaler().fit_transform(df[numerical])
df.to_csv('normalized_car.csv')  
