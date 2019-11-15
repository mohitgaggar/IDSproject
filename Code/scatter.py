import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("../Standardization/standardized_car.csv")
colors = ("red", "blue")
area = np.pi*3
# plt.scatter(df['Engine HP'],df['Engine Cylinders'])#,s=area,c=colors,alpha=0.5)
# plt.title('Scatter plot')
# plt.xlabel('Engine HP')
# plt.ylabel('Engine Cylinders')
# plt.show()

# plt.scatter(df['Engine HP'],df['Year'])#,s=area,c=colors,alpha=0.5)
# plt.title('Scatter plot')
# plt.xlabel('Engine HP')
# plt.ylabel('Year')
# plt.show()

# plt.scatter(df['highway MPG'],df['Engine Cylinders'])#,s=area,c=colors,alpha=0.5)
# plt.title('Scatter plot')
# plt.xlabel('highway MPG')
# plt.ylabel('Engine Cylinders')
# plt.show()

# plt.scatter(df['city mpg'],df['Engine Cylinders'])#,s=area,c=colors,alpha=0.5)
# plt.title('Scatter plot')
# plt.xlabel('city mpg')
# plt.ylabel('Engine Cylinders')
# plt.show()

plt.scatter(df['Engine HP'],df['Popularity'])#,s=area,c=colors,alpha=0.5)
plt.title('Scatter plot')
plt.xlabel('Engine HP')
plt.ylabel('Popularity')
plt.show()