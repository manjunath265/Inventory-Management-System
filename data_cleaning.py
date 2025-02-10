import pandas as pd 

file_path = r"C:/Users/manju/Downloads/sales_data_sample.csv"
data = pd.read_csv(file_path)

print(data.head())

data['ORDERDATE'] = pd.to_datetime(data['ORDERDATE'], errors = 'coerce')

data_cleaned = data.drop(columns=['ADDRESSLINE2', 'TERRITORY'])

data_cleaned['STATE'] = data_cleaned['STATE'].fillna('unknown')

data_cleaned = data_cleaned.dropna(subset=['POSTALCODE'])

data_cleaned = data_cleaned.drop_duplicates()

print(data_cleaned.isnull().sum())  # Check for missing values
print(data_cleaned.head()) 

cleaned_file_path = "C:/Users/manju/Downloads/sales_data_sample.csv"
data_cleaned.to_csv(cleaned_file_path,index=False)
print(f"Cleaned data saved to: {cleaned_file_path}")
