import numpy as np
import pandas as pd
import os
# Initial data path

#initial_data_path = os.path.join("data.csv")
# NaN value & directory path
#nan_directory_path = os.path.join("Desktop","nan")
#nan_data_path = os.path.join("d_car.csv")
# Percentage NaN
percentage_nan = [0.015, 0.03, 0.01] # The variable to keep track of what percent of data is modified to NaN

column_list1 = ['Make','Model','Year']
column_list2 = ['Engine Fuel Type','Engine HP','Engine Cylinders','Transmission Type']
column_list3 = ['Driven_Wheels','Number of Doors','Market Category','Vehicle Size','Vehicle Style' ,'highway MPG','city mpg','Popularity']

df = pd.DataFrame(pd.read_csv("data.csv"))

# Adding NaN
for col in column_list1:
	ori_rat = df[col].isna().mean()

	if ori_rat >= percentage_nan[0]:
		continue
	add_miss_rat = (percentage_nan[0] - ori_rat) / (1 - ori_rat)
	vals_to_nan = df[col].dropna().sample(frac=add_miss_rat).index
	df.loc[vals_to_nan, col] = np.nan

for col in column_list2:
	ori_rat = df[col].isna().mean()
	if ori_rat >= percentage_nan[1]:
		continue
	add_miss_rat = (percentage_nan[1] - ori_rat) / (1 - ori_rat)
	vals_to_nan = df[col].dropna().sample(frac=add_miss_rat).index
	df.loc[vals_to_nan, col] = np.nan

for col in column_list3:
	ori_rat = df[col].isna().mean()
	if ori_rat >= percentage_nan[2]: 
		continue
	add_miss_rat = (percentage_nan[2] - ori_rat) / (1 - ori_rat)
	vals_to_nan = df[col].dropna().sample(frac=add_miss_rat).index
	df.loc[vals_to_nan, col] = np.nan

# Filling NaN
df.fillna("NaN", inplace = True)
# Saving the new dataset
#os.mkdir(nan_directory_path) # making new directory to save newversion
df.to_csv("d_car.csv")
print("done") 






