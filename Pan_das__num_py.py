### DataFrame Creation, Show, Head, Tail, Info, Describe, Aggregation Function, Text Function, Where Class, Group By, Joins

# import pandas as pd
# df = pd.read_csv(r"C:\Users\NITHISH KUMAR\Music\First_10_record.csv")
# print(df)          ### Show all
# print(df.head())   ### Show first five rows
# print(df.head(3))  ### Show first three rows
# print(df.tail())   ### Show last five rows
# print(df.tail(2))  ### show last 2 rows

# print(df.to_string())
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe().to_string())


import pandas as pd
df = pd.read_csv(r"C:\Users\NITHISH KUMAR\Music\First_10_record.csv")

#### show()   --This shows every values to get all string values (df.to_string())
# print(df)
print(df.to_string())

# print(df.head())
# print(df.head().to_string())

# print(df.info())
# print(df.describe().to_string())

# print(df["Sales"].agg(["sum", "mean", "max", "min"]))
# print(df[df["Customer Name"].str.contains("a")].to_string())

##### Text Functions ( upper(), lower(), title(), capitalize(), swapcase() )
# print(df["Product Name"])   #----- for our convenience
# print(df["Product Name"].str.upper())
# print(df["Product Name"].str.lower())
# print(df["Product Name"].str.title())
# print(df["Product Name"].str.capitalize())
# print(df["Product Name"].str.swapcase())


# print(df["Product Name"].str.strip())   ## Remove both right and left spaces
# print(df["Product Name"].str.lstrip())   ## Remove only left spaces
# print(df["Product Name"].str.rstrip())    ## Remove only right spaces

# print(df['Product Name'].str.contains('a'))
# print(df[df["Product Name"].str.contains("a")].to_string())

#### Contains
# print(df['Customer Name'].str.containg('a'))
# print(df[df["Customer Name"].str.contains("a")].to_string())

#### Startswith, Endswith
# print(df['Customer Name'].str.startswith('L')])
# print(df['Customer Name'].str.startswith('L')])
# print(df[df['Customer Name'].str.startswith('L')].to_string())
# print(df[df['Customer Name'].str.endswith('n')].to_string())



### DataFrame Creation
# data =  {
#     "Name": ["A", "B", "C", "D"],
#     "Age": [1,2,3,4],
#     "Location": ['Chennai','Karur','Theni','Madurai']}
#
# df = pd.DataFrame(data)
# print(df)

# print(df.info()

##### Describe  (number, object, all)
# print(df.describe())
# print(df.describe().to_string())
# print(df["Sales"].describe().to_string())
# print(df["Sales"].describe())
# print(df.describe(include='all'))
# print(df.describe(include='all').to_string())
# print(df.describe(include='object'))
# print(df.describe(include='object').to_string())
# print(df.describe(include="number"))
# print(df.describe(include="number").to_string())


#####  Aggregation (Whole table and particular column also)
# print(df.count())
# print(df.min())
# print(df["Sales"].sum())
# print(df["Sales"].mean())
# print(df["Sales"].median())
# print(df["Sales"].min())
# print(df["Sales"].max())
# print(df["Sales"].count())
# print(df["Sales"].size)
# print(df["Sales"].std())
# print(df["Sales"].var())
# print(df["Sales"].prod())
# print(df["Sales"].sem())
# print(df["Sales"].quantile())
# print(df["Sales"].nunique())
# print(df["Sales"].idxmin())
# print(df["Sales"].idxmax())

# print(df['Order Priority'].str.casefold())
# print(df['Order Priority'].str.len())
# print(df['Order Priority'].str.find('a'))
# print(df['Order Priority'].str.rfind('a'))

# print(df['Order Priority'].str.index())       ## Doubt
# print(df['Order Priority'].str.rindex())      ## Doubt

# print(df['Order Priority'].str.replace("a","e"))
# print(df['Order Priority'].str.contains())
# print(df['Order Priority'].str.startswith())
# print(df['Order Priority'].str.endswith())
# print(df['Order Priority'].str.split())
# print(df['Order Priority'].str.get())
# print(df['Order Priority'].str.slice())
# print(df['Order Priority'].str.isalpha())
# print(df['Order Priority'].str.isdigit())
# print(df['Order Priority'].str.isalnum())
# print(df['Order Priority'].str.cat())


### Where class
# print(df[df["Sales"] > 1000])
# print(df[df["Sales"] > 1000].to_string())
# print(df["Sales"].where(df["Sales"] > 1000))
# print(df["Sales"].where(df["Sales"] > 1000,0))
# print(df["Sales"].where(df["Profit"] > 100,0))
# print(df["Sales"].where(df["Profit"] > 100))


### Group by
# print(df.groupby('Order Priority')["Sales"].min())
# print(df.groupby('Order Priority')["Sales"].sum())
