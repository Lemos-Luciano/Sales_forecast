
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
from fbprophet import Prophet


url_sales = "https://raw.githubusercontent.com/Lemos-Luciano/Sales_forecast/main/Dataset_Sales.csv"
url_stores = "https://raw.githubusercontent.com/Lemos-Luciano/Sales_forecast/main/Dataset_Stores.csv"

sales_train_df = pd.read_csv(url_sales)
store_info_df = pd.read_csv(url_stores)

      ###---------- 1) Cleaning of Sales Dataset ----------###
#I remove unnecessary data, so I remove data on closed stores since it does not provide me with useful information for the sales forecast
sales_train_df = sales_train_df[sales_train_df['Open'] == 1]

#I remove the Open column since it doesn't make sense, all the data we have is about open stores. So open = 1
sales_train_df.drop(["Open"], axis = 1, inplace=True) 


      ###---------- 2) Cleaning of Store Dataset ----------###
#There are several Na values, it is important to perform data cleaning. As a large part of the DataSet is null data, deleting the data is not an option, taking the average would not make sense (all the competitors opened on an average date? Quack!)
#So I'll replace it with 0
#CompetitionDistance does not make sense to replace it with the value 0 since we would be talking about ourselves. So we will put an average of the rest
str_cols = ("Promo2SinceWeek", "Promo2SinceYear", "PromoInterval", "CompetitionOpenSinceMonth",	"CompetitionOpenSinceYear")
for str in str_cols:
  store_info_df[str].fillna(0, inplace = True)  

store_info_df['CompetitionDistance'].fillna(store_info_df['CompetitionDistance'].mean(), inplace = True) 


      ###----------    3)  DATASET COBINATION     ----------###
sales_train_all_df = pd.merge(sales_train_df, store_info_df, how = 'inner', on = 'Store') #Both datasets share the 'store' column

##Our dataset in the Date column has all the data together (years, month and day), this is not the case with the store data, where the dates of the competitors are separated by year and month. I will create new columns from the Date column to separate date month and year
sales_train_all_df['Year'] = pd.DatetimeIndex(sales_train_all_df['Date']).year
sales_train_all_df['Month'] = pd.DatetimeIndex(sales_train_all_df['Date']).month
sales_train_all_df['Day'] = pd.DatetimeIndex(sales_train_all_df['Date']).day


     
      ###----------    4)  MODEL CREATION     ----------### 
# IMPORTANT!!! => WE WILL USE FBPROPHET IN THE MODEL, SO WE WILL HAVE TO INSTALL IT BEFOREHAND.
# For fbprophet to work properly we must install Pystan V2.19.1.1 (higher versions are not supported).
# For Pystan to work normally we must install the C++ compiler and dependencies (numpy and cython. Optional dependencies are: matplotlib, scipy and pandas)

#Guide to install pystan correctly "https://pystan2.readthedocs.io/en/latest/windows.html" => according to the guide for work correctly pystan the previous steps should be done with conda
# conda update conda #update conda package manager to the latest version
# conda install libpython m2w64-toolchain -c msys2 #Installing C++ compiler
# conda install numpy cython -c conda-forge #Installing dependencies
# conda install matplotlib scipy pandas -c conda-forge #Installing Optional dependencies 


#Having many pystan incompatibilities with fbprophet according to their versions, I remove the previous versions and install the appropriate ones without cache
# pip uninstall fbprophet pystan
# pip --no-cache-dir install pystan
# pip --no-cache-dir install fbprophet



def sales_predictions (Store_ID, sales_df, periods):
  sales_df = sales_df[sales_df['Store'] == Store_ID] #I want it to only analyze the data of the chosen store and not the entire dataset
  sales_df = sales_df[['Date', 'Sales']].rename(columns = {'Date' : 'ds', 'Sales' : 'y'}) #we must rename the date and sales column to the format requested by facebookprhopet (date has to be ds and sales has to be y) two square brackets [[]], the first to select the column and the second to indicate a list
  sales_df = sales_df.sort_values('ds')#sort them by ascending date

  #return sales_df   # I used to test
  model    = Prophet()
  model.fit(sales_df)
  future   = model.make_future_dataframe(periods = periods) 
  forecast = model.predict(future) #forecast is the value/calculation of sales itself
  figure   = model.plot(forecast, xlabel = 'Dates', ylabel = 'Sales')
  figure2  = model.plot_components(forecast) 

sales_predictions(10, sales_train_all_df, 60)
plt.show()