
import pandas as pd 


url_sales = "https://raw.githubusercontent.com/Lemos-Luciano/Sales_forecast/main/Dataset_Sales.csv"
url_stores = "https://raw.githubusercontent.com/Lemos-Luciano/Sales_forecast/main/Dataset_Stores.csv"

sales_train_df = pd.read_csv(url_sales)
store_info_df = pd.read_csv(url_stores)


