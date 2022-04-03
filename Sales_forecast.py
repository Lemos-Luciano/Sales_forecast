
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


url_sales = "https://raw.githubusercontent.com/Lemos-Luciano/Sales_forecast/main/Dataset_Sales.csv"
url_stores = "https://raw.githubusercontent.com/Lemos-Luciano/Sales_forecast/main/Dataset_Stores.csv"

sales_train_df = pd.read_csv(url_sales)
store_info_df = pd.read_csv(url_stores)


        ###----------    1)  SALES DATASET ANALYSIS     ----------###

sales_train_df.head(5)
sales_train_df.tail(5)
sales_train_df.info()
sales_train_df.describe()


#We graphically explore whether the sales dataset has null data. We observe the sales dataset doesn't contain null data since graphically it doesn't contain blue lines
sns.heatmap(sales_train_df.isnull(),yticklabels=False, cbar=False, cmap= "Blues" )


sales_train_df.hist(bins=30, figsize=(20,20), color = "r")
#plt.show()

#I check how many days the stores were open and how many closed
open_train_df = sales_train_df[sales_train_df['Open'] == 1]
closed_train_df = sales_train_df[sales_train_df["Open"] == 0]
print("The total number of open and closed stores are = {}".format(len(sales_train_df)))
print("The total number of open stores in the dataset is  = {}".format(len(open_train_df)))
print("The total number of closed stores in the dataset is = {}".format(len(closed_train_df)))
print(len(open_train_df)+len(closed_train_df))
print("The percentage of open stores is = {} %".format(round(100.0*len(open_train_df)/len(sales_train_df),2)))

#I remove unnecessary data, so I remove data on closed stores since it does not provide me with useful information for the sales forecast
sales_train_df = sales_train_df[sales_train_df['Open'] == 1]
sales_train_df

#I remove the Open column since it doesn't make sense, all the data we have is about open stores. So open = 1
sales_train_df.drop(["Open"], axis = 1, inplace=True)  #axis=1 removes the column, Inplace=True is to overwrite the dataframe
sales_train_df

sales_train_df.describe()
#Now we can see that by analyzing only the open stores we have more realistic data
# the average sales was 5,773 and is now 6,955
#The average number of clients was 633 and now 762




        ###----------    2)  STORE DATASET ANALYSIS     ----------###


store_info_df.head(5)
store_info_df.tail(5)
store_info_df.info()
store_info_df.describe()


#CompetitionDistance, CompetitionOpenSinceMonth/Year, Promo2SinceWeek/Year and PromoInterval have null data
sns.heatmap(store_info_df.isnull(),yticklabels=False, cbar=False, cmap= "Blues" )
#plt.show()

store_info_df[store_info_df['CompetitionDistance'].isnull()]
store_info_df[store_info_df['CompetitionOpenSinceMonth'].isnull()]
store_info_df[store_info_df["Promo2"] == 0] #"Promo2SinceWeek; Promo2SinceYear; PromoInterval" are Na since there was never a promotion in the store








