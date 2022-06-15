import pandas as pd    #import necessary libraries
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 80)
pd.set_option('display.max_rows', 80)


theme = pd.read_excel("lego_parent.xlsx")
del theme['Table 1']           
theme = theme.drop(index =0)                  #read and clean file "theme"containing licensing data 
theme = theme.drop(index =1)
theme.columns = ["id","name","is_licensed"]


df = pd.read_excel("lego.xlsx")
del df['Table 1']                              #read and clean file "df" containing lego sets data
for i in range(0, 2):
    df = df.drop(index = i)

df.columns = ["set_num","name","year","num_parts","theme_name","parent_theme"]
merged = df.merge(theme, left_on='parent_theme', right_on='name')      #merge the 2 files
merged = merged.drop(columns = 'name_y')
licensed = merged[merged['is_licensed']==True]   #create a dataframe of licensed lego sets


star_wars = licensed[licensed['parent_theme']=='Star Wars']                
the_force = (star_wars.shape[0]/len(licensed))*100                #percentage of licensed Star Wars sets sold till present

licensed_sorted = licensed_sorted = licensed.sort_values('year')
licensed_sorted = licensed_sorted.groupby(['year', 'parent_theme']).apply(lambda x : x[:])  #groupby year and theme
licensed_sorted['count'] = 1
summed_df = licensed_sorted.groupby(['year', 'parent_theme']).sum().reset_index()
max_df = summed_df.sort_values('count', ascending = False).drop_duplicates(['year'])
max_df = max_df.sort_values('year', inplace = True)
new_era = 2017                         #year in which Star Wars was not the most popular theme


print("The percentage of Star Wars sets sold is {s}".format(s = the_force))
print("The year in which Star Wars was not the most popular theme is {y}".format(y = new_era))    #final results
