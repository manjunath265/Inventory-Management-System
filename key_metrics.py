import pandas as pd 

file_path = r"C:\Users\manju\OneDrive\Documents\Desktop\sales_data_sample.csv"
df = pd.read_csv(file_path)
##TOTAL SALES
df['calculated_sales'] = df['QUANTITYORDERED']*df['PRICEEACH']
total_sales = df['calculated_sales'].sum()

print(f'Total Sales: ${total_sales:,.2f}')

## AVERAGE ORDER VALUE

total_orders = df['ORDERNUMBER'].nunique()

avg_order_value = total_sales / total_orders 

print(f'The Average order value {avg_order_value:,.2f}')

## GROWTH RATE 

df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"])

# Calculate sales per month
df["Calculated_Sales"] = df["QUANTITYORDERED"] * df["PRICEEACH"]
df["YEAR_MONTH"] = df["ORDERDATE"].dt.to_period("M")  # Extract Year-Month
monthly_sales = df.groupby("YEAR_MONTH")["Calculated_Sales"].sum()

# Compute sales growth rate
sales_growth_rate = monthly_sales.pct_change() * 100  # Percentage change

# Print results
print("Sales Growth Rate (%) per Month:")
print(sales_growth_rate.dropna())  # Drop NaN for the first month



## Top selling product

df['revenue'] = df['QUANTITYORDERED']*df['PRICEEACH']
total_revenue = df.groupby('PRODUCTLINE')['revenue'].sum()

top_selling_product = total_revenue.idxmax()
top_selling_product_revenue = total_revenue.max()


print(f"Top-Selling Product: {top_selling_product}")
print(f"Revenue: {top_selling_product_revenue}")