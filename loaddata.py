import pandas as pd
import numpy as np
import matplotlib.pyplot as plt      #import necessary libraries      
import os
import datetime as dt


all_months_data = pd.DataFrame()                 #create empty dataframe

files = [file for file in os.listdir("data_analysis")]
for file in files:                                                #read and modify excel files read from "data_analysis" folder
    df = pd.read_excel(os.path.join("data_analysis", file))
    all_months_data = pd.concat([all_months_data, df], ignore_index=True)


all_months_data = all_months_data.drop(index = 7)
all_months_data.columns = ["ORDER ID","Product name","Quantity ordered" ,"Price per piece","Order date"]
all_months_data=all_months_data.drop(index=0)
all_months_data['Month']=3
all_months_data['Month']=all_months_data['Order date'].astype(str).str[5:7]             #clean the data 
all_months_data['Month'].astype(int)
all_months_data['Price per piece'] = all_months_data['Price per piece'].astype(str).str.replace('$', '')
all_months_data['Price per piece'] = all_months_data['Price per piece'].astype(str).str.replace(',', '')



all_months_data['Price per piece'].astype(float)
a = np.array(all_months_data['Price per piece'], dtype = float)
b = np.array(all_months_data['Quantity ordered'], dtype = float)      #calculate the yearly sales from the data
c = np.multiply(a, b)
all_months_data['Sales']=c


plt.bar(all_months_data['Month'], all_months_data['Sales'])      #plot bar graph to find most profitable month
plt.show()


all_months_data['Order date(datetime)']=pd.to_datetime(all_months_data['Order date'])
all_months_data['Hour']=all_months_data['Order date(datetime)'].dt.hour                 #use datetime library 
all_months_data['minute']=all_months_data['Order date(datetime)'].dt.minute      



plt.bar(all_months_data['Hour'], all_months_data['Sales'])   #plot bar graph to find the hour of the day with most orders
plt.show()
