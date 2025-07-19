import pandas as pd
import json
import csv
df = pd.read_csv(r"EQ311023.CSV")
# print(df.columns)
#MAPPED CODES TO NAMES
key_value:dict ={}
company_list =[]
for index ,row in df.iterrows():
    key_value[row["SC_NAME"].strip()] = row["SC_CODE"]
    company_list.append(row["SC_NAME"].strip())

# RETURN CODE CMP VALUES
def get_company_code(company_name): 
    if company_name in key_value:
        return key_value[company_name]
    else:
        return None
# print(df.head())


# Write to CSV
with open('companies.csv', 'w', newline='') as csvfile:
   writer = csv.writer(csvfile)
   writer.writerow(['Company Name', 'Company Code'])  # Headers
   for name, code in key_value.items():
       writer.writerow([name, code])