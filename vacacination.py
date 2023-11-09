import csv
#
# Specify the path for the input CSV file
input_csv_file = 'vaccination-data.csv'
i=1
# Create an empty list to store the "country_name" values
country_names = []

# Open the input CSV file for reading with the correct encoding
with open(input_csv_file, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # Assuming "country_name" is the header in the CSV file
        country_name = row.get('COUNTRY')
        if country_name:
            print(country_name,i)
            i+=1
            country_names.append(country_name)

# Print the list of "country_name" values
for name in country_names:
    print(name)




# import pandas as pd
# csv_file = 'vaccination-data.csv'
# chunks = pd.read_csv(csv_file)
# countries = chunks.groupby("COUNTRY").sum()
# print(countries.columns)
# print(countries)




# import pandas as pd
# input_csv_file = 'vaccination-data.csv'
# df = pd.read_csv(input_csv_file, encoding='utf-8')
# row_indices = df.index.tolist()
# print("Row Indices:", row_indices)


# import pandas as pd
# input_csv_file = 'vaccination-data.csv'
# df = pd.read_csv(input_csv_file, encoding='utf-8')
# for i in range(1,228):
#     row_data = df.iloc[i]
#     if row_data['COUNTRY'':
#         print(row_data)
#         print(row_data['TOTAL_VACCINATIONS'])


# import pandas as pd
# input_csv_file = 'vaccination-data.csv'
# df = pd.read_csv(input_csv_file, encoding='utf-8')
# for i in range(0,228):
#     row_data = df.iloc[i]
#     print(row_data['COUNTRY'],end="\t")
#     print(row_data['TOTAL_VACCINATIONS'])
