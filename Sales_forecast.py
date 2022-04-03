
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime


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

store_info_df[store_info_df['CompetitionDistance'].isnull()] #
store_info_df[store_info_df['CompetitionOpenSinceMonth'].isnull()]
store_info_df[store_info_df["Promo2"] == 0] #"Promo2SinceWeek; Promo2SinceYear; PromoInterval" are Na since there was never a promotion in the store


#There are several Na values, it is important to perform data cleaning. As a large part of the DataSet is null data, deleting the data is not an option, taking the average would not make sense (all the competitors opened on an average date? Quack!)
#So I'll replace it with 0
#CompetitionDistance does not make sense to replace it with the value 0 since we would be talking about ourselves. So we will put an average of the rest
str_cols = ("Promo2SinceWeek", "Promo2SinceYear", "PromoInterval", "CompetitionOpenSinceMonth",	"CompetitionOpenSinceYear")
for str in str_cols:
  store_info_df[str].fillna(0, inplace = True)  #fillna => replace na values with the assigned value #inplace => does the substitution in memory and we should not create another variable

store_info_df['CompetitionDistance'].fillna(store_info_df['CompetitionDistance'].mean(), inplace = True) 

sns.heatmap(store_info_df.isnull(),yticklabels=False, cbar=False, cmap= "Blues" )
#plt.show()
store_info_df[store_info_df['Store'] == 291] #store 219 with clean data, well done!





        ###----------    3)  DATASET COBINATION     ----------###

sales_train_all_df = pd.merge(sales_train_df, store_info_df, how = 'inner', on = 'Store') #Both datasets share the 'store' column

sales_train_all_df.to_csv('CombinedDataset', index = False) #I save the new combined dataset
sales_train_all_df

#I correlate the data with sales since we want to know the effect it has on them
#We can see that sales have a high correlation with customers and the promo of the day, however, the more you increase the Promo2 (periodic promotions) decreases our amount of sales
correlations = sales_train_all_df.corr()['Sales'].sort_values() ##sort_values => will sort the data
correlations

correlations = sales_train_all_df.corr()
f, ax = plt.subplots(figsize = (20,20))
sns.heatmap(correlations, annot=True)
#plt.show()


##Our dataset in the Date column has all the data together (years, month and day), this is not the case with the store data, where the dates of the competitors are separated by year and month. I will create new columns from the Date column to separate date month and year
sales_train_all_df['Year'] = pd.DatetimeIndex(sales_train_all_df['Date']).year
sales_train_all_df['Month'] = pd.DatetimeIndex(sales_train_all_df['Date']).month
sales_train_all_df['Day'] = pd.DatetimeIndex(sales_train_all_df['Date']).day
sales_train_all_df



        ###----------    4) GRAPHICAL ANALYSIS OF THE COMBINED DATASET     ----------###

#we can see how sales are low in January and February, then increase but go down again in summer. Finally, at the holidays and Black Friday at the end of the year, it is where the largest number of sales is found.
axis = sales_train_all_df.groupby('Month')[['Sales']].mean().plot(figsize = (10, 5), marker = 'o', color = 'r')
axis.set_title('Average Sale per Month')
axis = sales_train_all_df.groupby('Month')[['Customers']].mean().plot(figsize = (10, 5), marker = '^', color = 'b')
axis.set_title('Average customers per Month')

#At the beginning and end of the month there are more sales, the 12th and 24th are the lowest
axis = sales_train_all_df.groupby('Day')[['Sales']].mean().plot(figsize = (10, 5), marker = 'o', color = 'r')
axis.set_title('Average sale per day')
axis = sales_train_all_df.groupby('Day')[['Customers']].mean().plot(figsize = (10, 5), marker = '^', color = 'b')
axis.set_title('Average customers per day')

#(1= Monday, 7=Sunday)
#I saw something strange, the number of customers on Monday is lower than on Sunday, however they have the same sales. Clearly the day with the most sales is Sunday and Saturday the lowest
axis = sales_train_all_df.groupby('DayOfWeek')[['Sales']].mean().plot(figsize = (10, 5), marker = 'o', color = 'r')
axis.set_title('Average sales per day of the week')
axis = sales_train_all_df.groupby('DayOfWeek')[['Customers']].mean().plot(figsize = (10, 5), marker = '^', color = 'b')
axis.set_title('Average Customers per day of the week')
#plt.show()


#Plot the sales according to the type of store and we can see that the type "B" store is the most profitable
fig, ax = plt.subplots(figsize = (20, 10))
sales_train_all_df.groupby(['Date','StoreType']).mean()['Sales'].unstack().plot(ax = ax)
#plt.show()


#We observe there is an increase in the number of customers and sales when the promotion exists
#Blue bar (0) = there is no promo, Orange bar (1) = There is a promo
plt.figure(figsize=[15, 10]) 
plt.subplot(211) 
sns.barplot(x = 'Promo', y = 'Sales', data = sales_train_all_df) 
plt.subplot(212) 
sns.barplot(x = 'Promo', y = 'Customers', data = sales_train_all_df) 


#In the violin graph you can see how when there is a promo there is a big difference in customers (the queue above), however there is not a big difference in sales
plt.figure(figsize=[15, 10]) 
plt.subplot(211)
sns.violinplot(x = 'Promo', y = 'Sales', data = sales_train_all_df) 
plt.subplot(212)
sns.violinplot(x = 'Promo', y = 'Customers', data = sales_train_all_df) 
plt.show()