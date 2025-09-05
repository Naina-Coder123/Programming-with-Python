import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("matplotlib_data.csv")
print(df.head())   # <- this will show output in the terminal
print(df.head(15))
print(df.describe())
print(df.info())
#create the line chart for sales
# df = pd.read_csv("matplotlib_data.csv")

df['Sales'].plot(kind='line', title='Line plot of sales')
plt.xlabel('Index')
plt.ylabel('Sales')
plt.show()

#create a plot to compare average sales per category
df.groupby('Category')['Sales'].mean().plot(
    kind='bar',
    color='skyblue',   # use a valid color
    title='Average sales per category'
)
plt.xlabel('Category')
plt.ylabel('Average Sales')
plt.legend()
plt.show() 

#create a plot to distribution of sales per category

category_sales = df.groupby('Category')['Sales'].sum()

category_sales.plot(
    kind='pie',
    autopct='%1.1f%%',   
    startangle=90,       
    figsize=(6,6),
    colormap='Set3'      
)

plt.title('Sales Distribution per Category')
plt.ylabel('')  
plt.show()
