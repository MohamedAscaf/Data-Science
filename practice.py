# import pandas as pd
# import matplotlib.pyplot as plt
import seaborn as sns

#corona_as = pd.read_csv('covid19_Confirmed_dataset.csv')
# print ('Modules imported')
# print(corona_as)
# print(corona_as.head(11))   #front
#print(corona_as.tail(11))   #back
#print(corona_as.shape)       #row_column
#print(corona_as.describe())

#corona_as_aggregated = corona_as.groupby('Country/Region').sum()
# corona_as_aggregated.loc['India'].plot()
# plt.legend()
# plt.show()

# corona_as_aggregated.loc ['Italy'].plot()
# plt.legend()
# plt.show()


# corona_as_aggregated.loc ['India'].diff().plot()
# plt.legend()
# plt.show()

# corona_as_aggregated.loc ['Italy'].diff().plot()
# plt.legend()
# plt.show()

# corona_as_aggregated.loc ['United Arab Emirates'].plot()
# plt.legend()
# plt.show()

# corona_as_aggregated.loc ['United Kingdom'].plot()
# plt.legend()
# plt.show()


#
# corona_as_aggregated.loc ['United Arab Emirates'].plot()
# corona_as_aggregated.loc['New Zealand'].plot()
# corona_as_aggregated.loc['India'].plot()
# corona_as_aggregated.loc['Italy'].plot()
# corona_as_aggregated.loc['Saudi Arabia'].plot()
# corona_as_aggregated.loc['US'].plot()
# corona_as_aggregated.loc['Switzerland'].plot()
# corona_as_aggregated.loc['Singapore'].plot()
# corona_as_aggregated.loc['Russia'].plot()
# corona_as_aggregated.loc['Qatar'].plot()
# corona_as_aggregated.loc['Japan'].plot()
# corona_as_aggregated.loc['Cuba'].plot()
# plt.legend()
# plt.show()


# df = corona_as.drop (['Lat','Long'], axis = 1)
# print(df)
#
# corona_as_aggregated.loc ['India'][:5].plot()
# plt.legend()
# plt.show()
#
#
# countries = list (corona_as_aggregated.index) # This will return the indices
# print(countries)
# max_infected_rates = []
# for c in countries :
#   max_infected_rates.append (corona_as_aggregated.loc[c]) # MAX INFECTION RATE OF ALL COUNTRIES
# # Directly append the numbers to the list using append () function
# print (max_infected_rates)



import pandas as pd
import matplotlib.pyplot as plt

corona_as = pd.read_csv('covid19_Confirmed_dataset.csv')
#print('modules imported')

corona_as_aggregated=corona_as.groupby("Country/Region").sum()

# print(corona_as_aggregated)
# for i in corona_as_aggregated:
#      print(i)

print(corona_as_aggregated.columns)
#
corona_as_aggregated.drop (['Province/State'], axis = 1, inplace = True)
print(corona_as_aggregated.columns)


print(corona_as_aggregated.loc['Canada'])
corona_as_aggregated.loc['Canada'].plot()

# # # corona_as_aggregated.loc['US'][:6].plot()
# # # corona_as_aggregated.loc()['United Arab Emirates'][:6].plot()
plt.legend()
plt.show()
#//////////////////////////////////////////
countries=list(corona_as_aggregated.index)
#
max_infected_rates=[]



for x in countries:
    if x in corona_as_aggregated.index:
        country_data = corona_as_aggregated.loc[x]

        # Convert the data to numeric type (float) if it's not already
        country_data = pd.to_numeric(country_data, errors='coerce')

        if not country_data.isna().all():
            max_diff = country_data.diff().max()
            max_infected_rates.append(max_diff)
            #print(f"Max difference for {country}: {max_diff}")

        else:
            print(f"No numeric data available for {x}")

#print(max_infected_rates)

corona_as_aggregated ['max_infected_rates'] = max_infected_rates
#print (corona_as_aggregated)

#data frame is a two dimesional array
corona_data = pd.DataFrame (corona_as_aggregated ['max_infected_rates'])
#print(corona_data)






worldwide_happiness_report = pd.read_csv ('worldwide_happiness_report.csv')
#print(worldwide_happiness_report)


#axis 1 is used to drop column and 0 is used to drop row
#inplace is true = replace the main also
worldwide_happiness_report.drop (['Freedom to make life choices','Generosity','Perceptions of corruption'], axis = 1, inplace = True)
#print(worldwide_happiness_report)

worldwide_happiness_report.set_index ('Country or region', inplace = True)
#print(worldwide_happiness_report)

data = corona_data.join (worldwide_happiness_report, how = 'inner')
#print(data)


#print(data.corr ())

# import numpy as np
# import matplotlib.pyplot as plt
#
# x_axis = data['Healthy life expectancy']
# y_axis = data['max_infected_rates']
# sns.scatterplot(x=x_axis, y=np.log(y_axis))
# sns.regplot (x=x_axis,y=np.log(y_axis))
# sns.catplot(x=x_axis,y=np.log(y_axis))
# sns.barplot(x=x_axis,y=np.log(y_axis))
# sns.boxenplot(x=x_axis,y=np.log(y_axis))
# plt.show()
