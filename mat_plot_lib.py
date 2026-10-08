# import matplotlib.pyplot as plt
# import numpy as np
#
# # a = np.array([1,2,3,4,5,6])
# # b = np.array([1,11,3,13,5,15])
# c = np.array([1,2,3,4,5,6])
# d = np.array([1,20,6,23,5,15])
#
# # plt.plot(c,d)
# # plt.plot(c,d,'o')
# # plt.plot(c,d,marker='*',linestyle='-',markersize=20 ,linewidth=10,mec='r',mfc='g')
# plt.plot(c,d,marker='*',linestyle='-',markersize=20 ,linewidth=10,mec='r',mfc='g', color='palepink')
#
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Get data from Power BI
df = pd.read_csv(r'C:\Users\NITHISH KUMAR\Music\First_10_record.csv')

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Group sales and profit by month
monthly = (
    df.groupby(df["Order Date"].dt.to_period("M"))
      [["Sales", "Profit"]]
      .sum()
      .reset_index()
)

# Convert period to string for plotting
monthly["Order Date"] = monthly["Order Date"].astype(str)

# Create figure
plt.figure(figsize=(12, 6))

# Sales line
plt.plot(
    monthly["Order Date"],
    monthly["Sales"],
    marker="o",
    label="Sales"
)

# Profit line
plt.plot(
    monthly["Order Date"],
    monthly["Profit"],
    marker="o",
    label="Profit"
)

# Titles and labels
plt.title("Superstore Monthly Sales and Profit")
plt.xlabel("Month")
plt.ylabel("Amount")

# Rotate month names
plt.xticks(rotation=45)

# Show legend
plt.legend()

# Grid
plt.grid(True, alpha=0.3)

# Adjust layout
plt.tight_layout()

# Display
plt.show()