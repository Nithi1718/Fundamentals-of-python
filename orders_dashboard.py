import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fontTools.ttLib.tables.otBase import CountReference

"""Using pandas i have performed these actions"""
# df =  pd.read_csv(r"C:\Users\NITHISH KUMAR\OneDrive\Desktop\Sample - Superstore Sales (Excel).csv")
# print(df.head().to_string())

# df['Sales'] = pd.to_numeric(df['Sales'],errors='coerce')
# df['Order Quantity'] = pd.to_numeric(df['Order Quantity'], errors='coerce')
# Region = df['Region']
# print(df['Sales'].head())

"""Now i use numpy to calculate the values"""
# Sales_value = df['Sales'].to_numpy()
# print("Sum of sales", np.sum(Sales_value))
# print("Average Sales", np.mean(Sales_value))
# print("Maximum Sales", np.max(Sales_value))
# print("Minimum Sales", np.min(Sales_value))


"""Using matplotlib for visualization"""
# x=df['Sales']
# y=Region
# plt.plot(x, y, marker='P', linestyle='--', mec='blue', mfc='green', color='red', linewidth=13, markersize=9)
# plt.show()

# plt.bar(df['Order Quantity'], df['Sales'])
# plt.show()


# """# import matplotlib.pyplot as plt
# # import numpy as np
# #
# # #plot 1:
# # x = np.array([0, 1, 2, 3])
# # y = np.array([3, 8, 1, 10])
# #
# # plt.subplot(2, 4, 8)
# # plt.plot(x,y)
# #
# # #plot 2:
# # x = np.array([0, 1, 2, 3])
# # y = np.array([10, 20, 30, 40])
# #
# # plt.subplot(2, 4, 7)
# # plt.plot(x,y)
# #
# # plt.subplot(2,4,3)
# # plt.bar(Region, df['Order Quantity'])
# #
# # plt.show()"""


df = pd.read_csv(r"C:\Users\NITHISH KUMAR\Music\Power BI\BMW\BMW_Sales_Data.csv")
print(df.head().to_string())
# print(df.count())

Regions = df['Region']
Countrys = df['Country']
Channels = df['Channel']
Quantity_Sold = pd.to_numeric(df['Quantity Sold'], errors='coerce')
Revenues = pd.to_numeric(df['Revenue'], errors='coerce')
Models = df['Model']
years = pd.to_datetime(df['Year'], errors='coerce')
Dates = pd.to_datetime(df['Date'], errors='coerce')

plt.subplot(3,3,1)
plt.bar(Quantity_Sold, Revenues, width=0.45, color='red')
plt.title('Revenue Buy Quantity')


plt.subplot(3,3,2)
plt.pie(Quantity_Sold, labels = Regions)



plt.show()

