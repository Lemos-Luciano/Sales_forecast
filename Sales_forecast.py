
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


url_sales = "https://raw.githubusercontent.com/Lemos-Luciano/Sales_forecast/main/Dataset_Sales.csv"
url_stores = "https://raw.githubusercontent.com/Lemos-Luciano/Sales_forecast/main/Dataset_Stores.csv"

sales_train_df = pd.read_csv(url_sales)
store_info_df = pd.read_csv(url_stores)


sales_train_df.head(5)
sales_train_df.tail(5)
sales_train_df.info()
sales_train_df.describe()

store_info_df.head(5)
store_info_df.tail(5)
store_info_df.info()
store_info_df.describe()

sns.heatmap(sales_train_df.isnull(),yticklabels=False, cbar=False, cmap= "Blues" )

sales_train_df.hist(bins=30, figsize=(20,20), color = "r")
plt.show()

#I check how many days the stores were open and how many closed
open_train_df = sales_train_df[sales_train_df['Open'] == 1]
closed_train_df = sales_train_df[sales_train_df["Open"] == 0]
print("The total number of open and closed stores are = {}".format(len(sales_train_df)))
print("The total number of open stores in the dataset is  = {}".format(len(open_train_df)))
print("The total number of closed stores in the dataset is = {}".format(len(closed_train_df)))
print(len(open_train_df)+len(closed_train_df))
print("The percentage of open stores is = {} %".format(round(100.0*len(open_train_df)/len(sales_train_df),2)))