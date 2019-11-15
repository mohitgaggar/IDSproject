import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("../Standardization/standardized_car.csv")

plt.boxplot(df["Engine HP"], showfliers=True, vert=False)   #to remove all the outliers
plt.show()