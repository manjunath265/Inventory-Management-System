import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned sales data
file_path = r"C:\Users\manju\OneDrive\Documents\Desktop\sales_data_sample.csv"
df = pd.read_csv(file_path)  

# Convert ORDERDATE to datetime format
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

# Aggregate Sales Data
# Daily Sales Trend
daily_sales = df.groupby('ORDERDATE')['SALES'].sum()

# Monthly Sales Trend
df['MONTH'] = df['ORDERDATE'].dt.to_period('M')
monthly_sales = df.groupby('MONTH')['SALES'].sum()

# Yearly Sales Trend
df['YEAR'] = df['ORDERDATE'].dt.year
yearly_sales = df.groupby('YEAR')['SALES'].sum()

# Plot Sales Trends

# Daily Sales Plot
plt.figure(figsize=(12, 5))
daily_sales.plot(title="Daily Sales Trend", color='blue', marker='o')
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.grid()
plt.show()  # Show the first plot
plt.clf()   # Clear the figure

# Monthly Sales Plot
plt.figure(figsize=(12, 5))
monthly_sales.plot(title="Monthly Sales Trend", color='green', marker='o')
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid()
plt.show()  # Show the second plot
plt.clf()   # Clear the figure

# Yearly Sales Plot
plt.figure(figsize=(8, 4))
yearly_sales.plot(kind='bar', title="Yearly Sales Trend", color='orange')
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()  # Show the third plot
plt.clf()   # Clear the figure

print("✅ Sales Data Aggregation and Trend Analysis Completed!")
