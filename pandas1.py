#pivot_table()


pd.pivot_table(
    data,
    values="Survived",
    index="Sex",
    columns="Pclass",
    aggfunc="mean"
)

##question - what are missing values aur use kitne tarike se fill kar sakte hain.
#Fill with a fixed value
data1["Age"] = data1["Age"].fillna(25)

data.isnull().sum()

data2['Age'].mean()

#Mean - Numerical Data
data2["Age"] = data2["Age"].fillna(data2["Age"].mean())

data2.isnull().sum()

#Median - Numerical Data : Usually better when there are outliers
data3["Age"] = data3["Age"].fillna(data3["Age"].median())

data3["Cabin"].mode()

data3.isnull().sum()

#Mode - Categorical Data : For categorical columns such as Gender,City,Department,
data3["Cabin"] = data3["Cabin"].filla(data3["Cabin"].mode()[0])


#Forward Fill - ffill() : Uses the previous value.Time-series data
data["Temperature"] = data["Temperature"].ffill()


#Backward Fill - bfill() : Uses the next availabale value : Time-series data
data["Temperature"] = data["Temperature"].bfill()


