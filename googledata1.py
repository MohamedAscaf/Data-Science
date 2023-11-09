import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import pandas as pd
#
# # Load a large CSV file in chunks
# chunk_size = 100000  # Adjust this as needed
# csv_file = 'aggregated.csv'
#
# chunks = pd.read_csv(csv_file, chunksize=chunk_size)
#
#
# num_rows = chunks.shape[0]
# print(num_rows)



# for chunk in chunks:
#     # Process each chunk of data
#     # Example: print the first few rows
#     print(chunk.head())




# dtypes = {'column_name_4': 'desired_dtype', 'column_name_95': 'desired_dtype', 'column_name_96': 'desired_dtype'}
# chunks = pd.read_csv(csv_file, chunksize=chunk_size, dtype=dtypes)
# chunks = pd.read_csv(csv_file, chunksize=chunk_size, low_memory=False)


# import pandas as pd
# csv_file = 'aggregated.csv'
# # Read the first 10 rows of the CSV file
# df = pd.read_csv(csv_file)
# # Now you have the first 10 rows in the DataFrame 'df'
# print(df)
#
# num_rows = df.shape[0]
# print(num_rows)
# df_as_string = df.to_string(index=False)  # You can remove the index if desired

# Print the DataFrame as a string
# print(df_as_string)


# file=open("file1.txt","a")
# file.write(df_as_string)



# import pandas as pd
# chunk_size = 100000
# csv_file = 'aggregated.csv'
# chunks = pd.read_csv(csv_file, chunksize=chunk_size)
# total_rows = 0
# for chunk in chunks:
#     total_rows += len(chunk)
#     print(total_rows)
# print("Total number of rows:", total_rows)
# Specify the paths for the input and output CSV files











#
#
#
# # Specify the paths for the input and output CSV files
# input_csv_file = 'aggregated.csv'
# output_csv_file = 'output.csv'
#
# # Define the range of rows to modify (100 to 200)
# start_row = 1000
# end_row = 1200
#
# # Open the input CSV file for reading
# with open(input_csv_file, 'r') as input_file:
#     # Read the content of the input file for the specified range of rows
#     csv_lines = [next(input_file) for _ in range(start_row - 1, end_row)]
#
# # Make changes to the selected rows (e.g., replace values)
# for i in range(len(csv_lines)):
#     # Check if the row index exists
#     if i < end_row - start_row + 1:
#         # Modify the row as needed
#         # For example, you can split the row into columns, make changes, and join them back
#         row_data = csv_lines[i].strip().split(',')
#         # Modify specific columns as needed
#         # Example: Replace the second column with 'ModifiedValue'
#         row_data[1] = 'ModifiedValue'
#         # Join the modified row data back to a CSV row
#         csv_lines[i] = ','.join(row_data) + '\n'
#
# # Open the output CSV file for writing
# with open(output_csv_file, 'a') as output_file:
#     # Write the modified content to the output file
#     output_file.writelines(csv_lines)
#
# print(f"Conversion from {input_csv_file} to {output_csv_file} completed for rows {start_row} to {end_row}.")
#
#

# # Specify the paths for the input and output CSV files
# input_csv_file = 'aggregated.csv'
# output_csv_file = 'output.csv'
#
# # Define the range of rows to modify (100 to 200)
# start_row = 100
# end_row = 200
#
# # Open the input CSV file for reading
# with open(input_csv_file, 'r') as input_file:
#     # Read the content of the input file for the specified range of rows
#     csv_lines = [next(input_file) for _ in range(start_row - 1, end_row)]
#
# # Make changes to the selected rows (e.g., replace values)
# for i in range(len(csv_lines)):
#     # Check if the row index exists
#     if i < end_row - start_row + 1:
#         # Modify the row as needed
#         # For example, you can split the row into columns, make changes, and join them back
#         row_data = csv_lines[i].strip().split(',')
#         # Modify specific columns as needed
#         # Example: Replace the second column with 'ModifiedValue'
#         row_data[1] = 'ModifiedValue'
#         # Join the modified row data back to a CSV row
#         csv_lines[i] = ','.join(row_data) + '\n'
#
# # Open the output CSV file for writing in append mode ('a')
# with open(output_csv_file, 'a') as output_file:
#     # Write the modified content to the output file
#     output_file.writelines(csv_lines)
#
# print(f"Appended data to {output_csv_file} for rows {start_row} to {end_row}.")





# #
# import csv
#
# # Specify the path for the input CSV file
# input_csv_file = 'aggregated.csv'
# print(1)
# # Define the row number you want to check
# row_number_to_check = 2000000  # Change this to the desired row number
#
# print(1)
# with open(input_csv_file, 'r', encoding='utf-8') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     i=1
#     for line_number, row in enumerate(csv_reader, start=1):
#         print(i)
#         i+=1
#         if line_number == row_number_to_check:
#             print("if")
#             # Found the row of interest
#             print(f"Row {row_number_to_check}: {','.join(row)}")
#             break  # Exit the loop after finding the row
#     else:
#         print("else")
#         # This code block will execute if the loop completes without finding the row
#         print(f"Row {row_number_to_check} not found in the CSV file.")








import csv

# Specify the path for the input CSV file
input_csv_file = 'aggregated.csv'
i=1
# Create an empty list to store the "country_name" values
country_names = []

# Open the input CSV file for reading with the correct encoding
with open(input_csv_file, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # Assuming "country_name" is the header in the CSV file
        country_name = row.get('country_name')
        if country_name:
            print(country_name,i)
            i+=1
            country_names.append(country_name)

# Print the list of "country_name" values
for name in country_names:
    print(name)
