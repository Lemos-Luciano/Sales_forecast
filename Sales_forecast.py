
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


url_sales = "https://raw.githubusercontent.com/Lemos-Luciano/Sales_forecast/main/Dataset_Sales.csv"
url_stores = "https://raw.githubusercontent.com/Lemos-Luciano/Sales_forecast/main/Dataset_Stores.csv"

sales_train_df = pd.read_csv(url_sales)
store_info_df = pd.read_csv(url_stores)


#I remove unnecessary data, so I remove data on closed stores since it does not provide me with useful information for the sales forecast
sales_train_df = sales_train_df[sales_train_df['Open'] == 1]

#I remove the Open column since it doesn't make sense, all the data we have is about open stores. So open = 1
sales_train_df.drop(["Open"], axis = 1, inplace=True)  #axis=1 removes the column, Inplace=True is to overwrite the dataframe
