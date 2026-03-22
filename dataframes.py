import numpy as np
import pandas as pd

data1 = {
    "name":["Sumit", "Karan", "Prem", "Vishal"],
    "marks":[90,88,96,59],
    "City":["Ghotki","Mithi","Kashmore","Quetta"],
    "Address":[np.nan,np.nan,np.nan,np.nan]
}

df = pd.DataFrame(data1)
print(df)
print(df.head(1))
print(df.tail(1))
print(df.describe())
# print(df.to_csv("Friends.csv"))
# print(df.to_csv("Friends2.csv",index=False))

shop_data = pd.read_csv('Shop.csv')
print(shop_data)

print(shop_data["Revenue"][3])

# shop_data["Revenue"][3] = 3280.66
# print(shop_data.to_csv("Shop.csv"))

shop_data.index = np.arange(1,11,1)
print(shop_data)

ser = pd.Series(np.random.rand(34)*100)
print(ser)
print(type(ser))

df2 = pd.DataFrame(np.random.rand(334,5)*100,index = np.arange(1,335,1))
print(df2.head(10))
print(df2.tail(10))
print(df2.describe())
print(type(df2))

df2[0][1] = "Sumit"

print(df2.head(2))
print(df2.dtypes)

df2.columns = list("ABCDE")

print(df2.head(2))

# 1st and 2nd row and C and D column
print(df2.loc[[1,2],["C","D"]])

# column A values should be less than 30 and C values should be greater than 50 
# print(df2.loc[(df2['A']<30) & (df2['C']>50)])

# first row and 5th column
print(df2.iloc[0,4])

# 1st and 5th row and 2nd and 3rd column
print(df2.iloc[[0,4],[1,2]])
print(df2.drop(1)) #1st row dropped
print(df2.drop(["A"],axis=1,inplace=True)) #A column dropped
print(df2.head())
print(df2.drop([1,5],axis=0,inplace=True)) #A column dropped
print(df2.head())
print(df2.reset_index())

print(shop_data.isnull())
shop_data.dropna(inplace=True)
# print(shop_data.to_csv("Shop.csv"))

print(df)
df.dropna(how="all",axis=1,inplace=True) # remove coulumns whose all values are none 
print(df)





