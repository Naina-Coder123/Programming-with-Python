#Pandas is a popular open-source Python library for data analysis and manipulation. It provides powerful, flexible data structures—mainly DataFrame and Series—that make it easy to clean, explore, and analyze data.

# Why use Pandas?
# Tabular Data Handling: Easily work with data in rows and columns (like spreadsheets or SQL tables).
# Data Cleaning: Handle missing data, filter rows, and transform columns.
# Data Analysis: Perform statistical calculations, group data, and aggregate results.
# File I/O: Read and write data from CSV, Excel, SQL databases, and more.
# Integration: Works well with other libraries like NumPy, Matplotlib, and Scikit-learn.

#numpy allows only homogemous characters 
# In pandas if i look in column level in each column one specific tye of value is there but at row level there is hetrogenous values in that row For example:
#Pandas work with labeled data i.e every column has name called label but in numpy data was unlabeled
#Pandas support different reperesentations:

#Series :1 D representation
#Dataframes: 2D representation
#Panel :3D representation
#Panel 4D:4D reperesetation

#in 2D reperesentation we concatenate two 1 D repersentation
# For example colum1 :age column2:name when concate age name it will give the one table

#create a series with following elements using the list
import pandas as pd
s1=pd.Series([10,20,30,40])
print(s1)
s2=pd.Series([10,20,30,40],index=['a','b','c','d'])
print(s2);

s3=pd.Series({"a":10,"b":20,"c":30,"d":40})
print(s3)

# create a series using scaler
# same value for each index in one go
s4=pd.Series(5,index=['a','b','c','d'])
print(s4)

#access the second element from s3 
print(s3[1])
print(s3['c'])

#vector operations
s5=s1+s3
print(s5)
s6=s3+s4
print(s6) # pyright: ignore[reportUndefinedVariable]

s7=pd.Series([20,30,40,50],index=['a','d','f','g'])
s8=s4+s7
print(s8)

#create a data frame to store the studemt personal details like first name, last name, age ,city
#store the details of atleast 5 students

dict={"firstname":["Naina","Deepa","Devanshi","Raj","Rahul"],"lastname":["Mishra","Patel","Awasthi","Bhaudauria","Goenka"],"age":[18,45,24,35,23],"city":["Kanpur","Kanpur","Kanpur","Lucknow","Lucknow"]}
print(dict)
#this is not declaring the tabular reperesentation
#but this dict will become the input for dataframe

# f1=pd.DataFrame({"Firstname":["Naina","Deepa","Devanshi","Raj","Rahul"],"Lastname":["Mishra","Patel","Awasthi","Bhaudauria","Goenka"],"Age":[18,45,24,35,23],"City":["Kanpur","Kanpur","Kanpur","Lucknow","Lucknow"]})
# print(f1)

d1=pd.Series(["Naina","Deepa","Devanshi","Raj","Rahul"])
d2=pd.Series(["Mishra","Patel","Awasthi","Bhaudauria","Goenka"])
d3=pd.Series([18,45,24,35,23])
d4=pd.Series(["Kanpur","Kanpur","Kanpur","Lucknow","Lucknow"])

d5=pd.DataFrame({"First_name":d1,"Last_name":d2,"Age":d3,"City":d4})
print(d5)
#print the age of the student
print(d5["Age"])
print(d5[["Last_name","City"]])

#find the details of student who lives in kanpur
d6=d5[d5["City"]=="Kanpur"]#mass
print(d6)
d7=[d5["City"]=="Kanpur"]
print(d7)
# find the details of student greater than 20
d8=d5[d5["Age"]>20]#mass
print(d8)

df=[d5["Age"]>20],d5["First_name"]
print(df)
# find first name and last name of students where age is greater than 20
df1=d5[d5["Age"]>20][["First_name","Last_name"]]
print(df1)

#delete null values from series
s5.dropna()
print(s5)
# if i will blindly apply drona() on the dataframe it will delete the entire row if any of the entry is Nan so it will abruptly delete the most of the entire dataset
s8.fillna(0)
print(s8)
#loc for label
# iloc for integer index

#find the first name and age who lives in lucknow
# using loc method
df2=d5[d5["City"]=="Lucknow"].loc[:,["First_name","Age"]]
print(df2)

df3=d5[d5["City"]=="Lucknow"].iloc[:,[0,2]]
print(df3)
print(d5.head())#give records from the begining
print(d5.head(2))
d5.info()
print(d5)

