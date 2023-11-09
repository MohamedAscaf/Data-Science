# import pandas as pd
# import matplotlib.pyplot as plt
#
#
# corona_as = pd.read_csv('covid19_Confirmed_dataset.csv')
# print ('Modules imported')
# print(corona_as)
# print(corona_as.head(11))   #front
# print(corona_as.tail(11))   #back
# print(corona_as.shape)       #row_column
# print(corona_as.describe())
#
# corona_as_aggregated = corona_as.groupby('Country/Region').sum()
# corona_as_aggregated.loc['India'].plot()
# plt.legend()
# plt.show()
#
# corona_as_aggregated.loc ['Italy'].plot()
# plt.legend()
# plt.show()
#
#
# corona_as_aggregated.loc ['India'].diff().plot()
# plt.legend()
# plt.show()
#
# corona_as_aggregated.loc ['Italy'].diff().plot()
# plt.legend()
# plt.show()
#
# corona_as_aggregated.loc ['United Arab Emirates'].plot()
# plt.legend()
# plt.show()
#
# corona_as_aggregated.loc ['United Kingdom'].plot()
# plt.legend()
# plt.show()
#
#
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
#
#
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





# import pandas as pd
# import matplotlib.pyplot as plt
#
# corona_as = pd.read_csv('covid19_Confirmed_dataset.csv')
# # print('modules imported')
#
# corona_as_aggregated = corona_as.groupby("Country/Region").sum()
#
# countries = list(corona_as_aggregated.index)
# max_infected_rates = []
#
# for x in countries:
#     if x in corona_as_aggregated.index:
#         country_data = corona_as_aggregated.loc[x]
#
#         country_data = pd.to_numeric(country_data, errors='coerce')
#
#         if not country_data.isna().all():
#
#             max_diff = country_data.diff().max()
#
#             max_infected_rates.append(max_diff)
#
#         else:
#             print(F"No numeric data available for {x}")

 #print(max_infected_rates)

# corona_as_aggregated['max_infected_rates'] = max_infected_rates
# print(corona_as_aggregated)
#
# corona_data = pd.DataFrame(corona_as_aggregated['max_infected_rates'])
# print(corona_data)
# #
# worldwide_happiness_report = pd.read_csv('worldwide_happiness_report.csv')
# # print(worldwide_happiness_report)
#
# worldwide_happiness_report.drop(['Freedom to make life choices', 'Generosity',
#                                  'Perceptions of corruption'], axis=1,
#                                 inplace=True)
# # print(worldwide_happiness_report)
#
# worldwide_happiness_report.set_index('Country or region',inplace = True)
#
# data = corona_data.join(worldwide_happiness_report, how='inner')
# #print(data)
#
# print(data.corr())
#
#
# import numpy as np
# import seaborn as sns
# x_axis = data['Social support']
# y_axis = data['max_infected_rates']
# sns.scatterplot(x=x_axis,y=np.log(y_axis))
# sns.regplot(x=x_axis,y=np.log(y_axis))
# sns.catplot(x=x_axis,y=np.log(y_axis))
# sns.barplot(x=x_axis,y=np.log(y_axis))
# sns.boxenplot(x=x_axis,y=np.log(y_axis))
# plt.show()





# import pandas as pd
# import matplotlib.pyplot as plt
#
# corona_as = pd.read_csv('covid19_Confirmed_dataset.csv')
# corona_as_aggregated = corona_as.groupby("Country/Region").sum()
# # print(corona_as_aggregated.columns)
# #
# corona_as_aggregated.drop(['Province/State'], axis=1, inplace=True)
# # print(corona_as_aggregated.columns)
# print(corona_as_aggregated.loc['China'])
# corona_as_aggregated.loc['China'].plot()
# print(corona_as_aggregated.loc['US'])
# plt.legend()
# plt.show()








#Vaccination

# import csv
# input_csv_file = 'vaccination-data.csv'
# i=1
# country_names = []
# with open(input_csv_file,'r',encoding = 'utf-8') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#          country_name = row.get('COUNTRY')
#          if country_name:
#              print (country_name,i)
#              i+=1
#              country_names.append(country_name)
# print("--------------------------------------------------")
#
# for name in country_names:
#     print(name)



# import pandas as pd
# csv_file = 'vaccination-data.csv'
# check = pd.read_csv(csv_file)
# countries = check.groupby("COUNTRY").sum()
# print(countries.columns)
# print(countries)



# import pandas as pd
# input_csv_file = 'vaccination-data.csv'
# df = pd.read_csv(input_csv_file,encoding = 'utf-8')
# for x in range(1,228):
#     row_data = df.iloc[x]
#     if row_data['COUNTRY']=='Canada':
#         print(row_data)
#         print(row_data['TOTAL_VACCINATIONS'])


# import pandas as pd
# input_csv_file = 'vaccination-data.csv'
# df = pd.read_csv(input_csv_file,encoding = 'utf-8')
# for x in range(1,228):
#     row_data = df.iloc[x]
#     if row_data['COUNTRY']=='Canada' or row_data['COUNTRY']=='India':
#         print(row_data)
#         print(row_data['TOTAL_VACCINATIONS'])
#         print("---------------------------------------")

# import pandas as pd
# input_csv_file = 'vaccination-data.csv'
# df = pd.read_csv(input_csv_file,encoding = 'utf-8')
# for x in range (0,228):
#     row_data = df.iloc[x]
#     print(row_data['COUNTRY'],end="\t")
#     print(row_data['TOTAL_VACCINATIONS'])






#Example DataSet

# import pandas as pd
# import matplotlib.pyplot as plt
#
# corona_md = pd.read_csv('vaccination-metadata.csv')
# print('Modules imported')


# print(corona_md.head(11))
# print(corona_md.tail(11))
# print(corona_md.shape)
# print(corona_md.describe())


# corona_md_aggregated = corona_md.groupby('ISO3').sum()
# # print(corona_md_aggregated)
# # print(corona_md)
# for i in range(0,1105):
#      row_data = corona_md.iloc[i]
#      if(row_data['ISO3']=="IND"):
#          print(row_data['ISO3'],end="\t")
#          print(row_data['VACCINE_NAME'])

# corona_md_aggregated = corona_md.groupby('ISO3').sum()
# for i in range(0,1105):
#     row_data = corona_md.iloc[i]
#     if(row_data['ISO3']=="DZA"):
#         print(row_data['ISO3'],end="\t")
#         print(row_data['VACCINE_NAME'],end="\t")
#         print(row_data['PRODUCT_NAME'])




#vaccination data

import pandas as pd
import matplotlib.pyplot as plt
corona_vd = pd.read_csv ('vaccination-data.csv')

print('Modules imported')
print(corona_vd)
print(corona_vd.head(11))
print(corona_vd.tail(11))
print(corona_vd.shape)
print(corona_vd.describe())

df = corona_vd.drop(['ISO3','DATA_SOURCE','DATE_UPDATED',
                     'VACCINES_USED','FIRST_VACCINE_DATE','NUMBER_VACCINES_TYPES_USED',
                     'PERSONS_BOOSTER_ADD_DOSE','PERSONS_BOOSTER_ADD_DOSE_PER100'],axis=1)
print(df)


df_aggregated = df.groupby('WHO_REGION').sum()

#
# df_aggregated.loc['Albania'].plot()
# plt.legend()
# plt.show()
#
# df_aggregated.loc['Japan'].plot()
# plt.legend()
# plt.show()
#
# df_aggregated.loc['Albania'].diff().plot()
# plt.legend()
# plt.show()
#
# df_aggregated.loc['Japan'].diff().plot()
# plt.legend()
# plt.show()


df_aggregated.loc['Albania'].plot()
df_aggregated.loc['Japan'].plot()
df_aggregated.loc['Hungary'].plot()
df_aggregated.loc['Denmark'].plot()
df_aggregated.loc['India'].plot()
df_aggregated.loc['Viet Nam'].plot()
df_aggregated.loc['Lebanon'].plot()
df_aggregated.loc['Armenia'].plot()
df_aggregated.loc['Malaysia'].plot()
df_aggregated.loc['Myanmar'].plot()
df_aggregated.loc['Austria'].plot()
df_aggregated.loc['Maldives'].plot()
df_aggregated.loc['China'].plot()
df_aggregated.loc['United States of America'].plot()
df_aggregated.loc['Brazil'].plot()
df_aggregated.loc['Indonesia'].plot()

plt.legend()
plt.show()
#
countries = list(df_aggregated.index)
print(countries)

max_infected_rates = []
for x in countries:
  max_infected_rates.append(df_aggregated.loc[x])

  print(max_infected_rates,end="******************************************")



