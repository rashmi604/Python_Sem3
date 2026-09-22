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

pip install requests


import pandas as pd
df = pd.read_csv(r'"C:\Users\Rashmi\Downloads\Titanic-Dataset.csv")
df.head(20)
df.tail(10)
df.info()
df.shape()


data.corr(numeric_only = True)##work only on numeric data not on objective columns
data.columns##provide names of all columns
data.iloc[0]##print values of first row of your data
data.iloc[10:21]#print values of row 10 to 20 dont include 21
data.iloc[10:21,0:4]#print values of row 10 to 20 dont include 21 and columns from 0 to 3 excluding 4
data['Age']## print all the values of age column(to check an individual column)
data.loc[data["Age"]>50] #print coluumns with age > 50
data['Pclass'],value_counts() # print counts to values
data.loc[data["Pclass"]==2], ["Name","Age","Sex","Cabin"]# print value of these columns

#Rename Columns
data.rename(columns={
    "PassengerId": "Passenger_ID",
    "Survived": "Survival"
}, inplace=True)

data['Parch'] value counts

data["Age"].mean()
data["Age"].median()
data["Age"].mode()
data["Age"].std()

data.groupby("Sex")["Age"].mean()

data.groupby("Pclass").agg({
    "Age": "mean",
    "Fare": "mean",
    "Survival": "sum"
})








