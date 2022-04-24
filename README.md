<h1 align="center">Hi 👋, I'm Luciano Lemos</h1>
<h3 align="center">For more information about me:</h3>

- 👨‍💻 All of my projects are available at [https://github.com/Lemos-Luciano](https://github.com/Lemos-Luciano)

- 📫 How to reach me **llemos@uoc.edu**

- 📄 Know about my experiences [https://github.com/Lemos-Luciano/Introduction/blob/516cce9ffad987352ba175f17a87ad2a78d96cc9/Resume_LucianoLemos.pdf](https://github.com/Lemos-Luciano/Introduction/blob/516cce9ffad987352ba175f17a87ad2a78d96cc9/Resume_LucianoLemos.pdf)

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://linkedin.com/in/luciano-lemos/?locale=en_us" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="luciano-lemos/?locale=en_us" height="30" width="40" /></a>
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://seaborn.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" alt="seaborn" width="40" height="40"/> </a> </p>



<h1 align="center">ABOUT THIS PROJECT</h1>

From the sales summary of the last 2 and a half years and the characteristics of the Rossmann stores (obtained from https://www.kaggle.com/c/rossmann-store-sales/data), with the use of fbprophet I developed a model that will allow us to predict future sales


The model is used as follows: **sales_predictions (Store_ID, sales_df, holidays, periods)**

**Store_ID** => Store number from which we want to predict sales <br>
**Sales_df** => Dataset that we will use (in this case sales_train_all_df) <br>
**Holidays** => Holidays that we will add to the model (in this case it have holidays at the state level and schools, so we will use the school_state_holidays dataset) <br>
**Periods** => Period to predict by the model (30|60|90 days, etc)


**Files:** 
- Dataset_Stores
- Dataset_Sales


  
**Data fields:**
- Id - an Id that represents a (Store, Date) duple within the test set
- Store - a unique Id for each store
- Sales - the turnover for any given day (this is what you are predicting)
- Customers - the number of customers on a given day
- Open - an indicator for whether the store was open: 0 = closed, 1 = open
- StateHoliday - indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. Note that all schools are closed on public   holidays and weekends. a = public holiday, b = Easter holiday, c = Christmas, 0 = None
- SchoolHoliday - indicates if the (Store, Date) was affected by the closure of public schools
- StoreType - differentiates between 4 different store models: a, b, c, d
- Assortment - describes an assortment level: a = basic, b = extra, c = extended
- CompetitionDistance - distance in meters to the nearest competitor store
- CompetitionOpenSince[Month/Year] - gives the approximate year and month of the time the nearest competitor was opened
- Promo - indicates whether a store is running a promo on that day
- Promo2 - Promo2 is a continuing and consecutive promotion for some stores: 0 = store is not participating, 1 = store is participating
- Promo2Since[Year/Week] - describes the year and calendar week when the store started participating in Promo2
- PromoInterval - describes the consecutive intervals Promo2 is started, naming the months the promotion is started anew. E.g. "Feb,May,Aug,Nov" means each round starts in February, May, August, November of any given year for that store
