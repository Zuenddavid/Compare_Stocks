from matplotlib import pylab as plt
import pandas as pd
import numpy as np
from datetime import datetime

# pd.plotting.register_matplotlib_converters()

df1 = pd.read_csv("/Users/davidzund/Library/Containers/com.microsoft.Excel/Data/Downloads/BX-4.csv")
print(df1)
df1['Date'] = pd.to_datetime(df1.Date)
# print(df1.head())

df2 = pd.read_csv("/Users/davidzund/Library/Containers/com.microsoft.Excel/Data/Downloads/BLK.csv")
print(df2)
df2['Date'] = pd.to_datetime(df2.Date)

df3 = pd.read_csv("/Users/davidzund/Library/Containers/com.microsoft.Excel/Data/Desktop/OGGG.csv")
print(df3)
df3['Date'] = pd.to_datetime(df3.Date)


mean = df1["Close"].mean()
mean2 = df2["Close"].mean()
mean3 = df3["Close"].mean()
# Plotting three stocks without any adjustment
# plt.figure("BlackStone / Blackrock / Partners Group not adjusted")
# plt.title("BlackStone / Blackrock / Partners Group not adjusted")
# plt.plot(df1["Date"], df1["Close"], 'r-', linewidth=0.6, label="Blackrock Stock price, mean="+str(mean))
# plt.plot(df2["Date"], df2["Close"], 'r-', linewidth=0.6, label="Blackstone Stock price, mean="+str(mean2), color = "green")
# plt.plot(df3["Date"], df3["Close"], 'r-', linewidth=0.6, label="Partners Group Stock price, mean="+str(mean3), color = "blue")
# plt.xlabel("Dates")
#plt.annotate('COVID -19 Crisis', xy=(2020, 900), xytext=(2020, 1000), fontsize=12,arrowprops=dict(facecolor='green', shrink=0.05))
# plt.ylabel("Prices in USD")
# plt.legend(loc="upper left")
# plt.show()
# Plotting three stocks with price adjustment
plt.figure("BlackStone / Blackrock / Partners Group adjusted")
plt.title("BlackStone / Blackrock / Partners Group price adjusted")
plt.plot(df1["Date"], df1["Close"]*10, 'r-', linewidth=0.6, label="Blackrock Stock price, mean="+str(mean))
plt.plot(df2["Date"], df2["Close"]*1.5, 'r-', linewidth=0.6, label="Blackstone Stock price, mean="+str(mean2), color = "green")
plt.plot(df3["Date"], df3["Close"], 'r-', linewidth=0.6, label="Partners Group Stock price, mean="+str(mean3), color = "blue")
plt.axvspan(datetime(2020, 2, 1), datetime(2020, 4, 15), facecolor='red', alpha=0.25)
plt.axvspan(datetime(2022, 2, 1), datetime(2022, 3, 15), facecolor='red', alpha=0.25)
plt.annotate('COVID -19 Crisis', xy=(2020, 900), xytext=(2020, 1000), fontsize=12,arrowprops=dict(facecolor='green', shrink=0.05))
plt.ylabel("Prices in USD")
plt.legend(loc="upper left")
plt.show()
