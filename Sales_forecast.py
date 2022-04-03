
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
sales_train_df.drop(["Open"], axis = 1, inplace=True) 

#There are several Na values, it is important to perform data cleaning. As a large part of the DataSet is null data, deleting the data is not an option, taking the average would not make sense (all the competitors opened on an average date? Quack!)
#So I'll replace it with 0
#CompetitionDistance does not make sense to replace it with the value 0 since we would be talking about ourselves. So we will put an average of the rest
str_cols = ("Promo2SinceWeek", "Promo2SinceYear", "PromoInterval", "CompetitionOpenSinceMonth",	"CompetitionOpenSinceYear")
for str in str_cols:
  store_info_df[str].fillna(0, inplace = True)  

store_info_df['CompetitionDistance'].fillna(store_info_df['CompetitionDistance'].mean(), inplace = True) 

