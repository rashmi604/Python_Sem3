pip install pandas
import pandas as pd
marks = pd.Series([80,90,95,88]) # Series(1D)
print(marks)

import pandas as pd
data = {
    "Name": ["Vikky","Rahul","Aman"],
    "Age": [22,21,32],
    "Marks": [89,98,76]
}
df = pd.DataFrame(data)

df = pd.read_csv('xyz.csv') # to read a csv file
data.head() # to print first 5 rows
data.tail() # to print last 5 rows
data.shape() #size of data (rows,columns)
data.info() # value of columns and their datatypes
data.columns()# to print name of each column of the data
data.describe() # tell mathematical relations
data.correlation() # find relation between two individual columns only for integers
data.duplicated().Sum() # how many duplicate values in a data
data.isnull().Sum()  #how many missing values in overall data

pip install requests # 

