
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import numpy as np
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
#Detailed guide in the Model branch

def sales_predictions (Store_ID, sales_df, holidays, periods):
  sales_df = sales_df[sales_df['Store'] == Store_ID] #I want it to only analyze the data of the chosen store and not the entire dataset
  sales_df = sales_df[['Date', 'Sales']].rename(columns = {'Date' : 'ds', 'Sales' : 'y'}) #we must rename the date and sales column to the format requested by facebookprhopet (date has to be ds and sales has to be y) two square brackets [[]], the first to select the column and the second to indicate a list
  sales_df = sales_df.sort_values('ds')#sort them by ascending date

  #return sales_df   # I used to test
  model    = Prophet(holidays = holidays) #by default holidays comes = none, so we say that now it is equal to the variable added above
  model.fit(sales_df)
  future   = model.make_future_dataframe(periods = periods) 
  forecast = model.predict(future) #forecast is the value/calculation of sales itself
  figure   = model.plot(forecast, xlabel = 'Dates', ylabel = 'Sales')
  figure2  = model.plot_components(forecast)

school_holidays = sales_train_all_df[sales_train_all_df['SchoolHoliday'] == 1].loc[:, 'Date'].values #get all dates related to school holidays
school_holidays = np.unique(school_holidays) #I remove the duplicate data to minimize the load
school_holidays = pd.DataFrame({'ds' : pd.to_datetime (school_holidays), 'holiday' : 'School Holiday'})

#I created a dataset with the state holidays that there are 3 holidays. REMEMBER, StateHoliday: Indicates if the day was a holiday or not (a = public holidays, b = Easter holidays, c = Christmas, 0 = It was not a holiday)
state_holidays = sales_train_all_df[(sales_train_all_df['StateHoliday'] == 'a') | (sales_train_all_df['StateHoliday'] == 'b') | (sales_train_all_df['StateHoliday'] == 'c')].loc[:, 'Date'].values
state_holidays = np.unique(state_holidays)
state_holidays = pd.DataFrame({'ds' : pd.to_datetime (state_holidays), 'holiday' : 'State Holiday'})

school_state_holidays = pd.concat((school_holidays, state_holidays), axis = 0) #combine the two datasets


      ###----------    4)  EXAMPLES    ----------### 
#stores number 10 the next 60 days of the dataset
sales_predictions(10, sales_train_all_df, school_state_holidays, 60)

#stores number 6 the next 90 days of the dataset
sales_predictions(6, sales_train_all_df, school_state_holidays, 90)
plt.show()
