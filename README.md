# E-commerce Inventory Management Analysis
## Project Overview

This project focuses on analyzing inventory and sales data using SQL, Python, and Power BI to extract insights that help businesses optimize their stock levels, track sales trends, and improve customer engagement.

## Objectives
Analyze total sales and revenue trends.
Identify fast-moving vs. slow-moving products.
Understand customer purchase behavior.
Optimize inventory restocking decisions.
Visualize insights using Power BI dashboards.



### Understanding the Dataset
**Objective**: Explore the dataset to understand its structure and key columns.

**Actions Completed**:
- Loaded and inspected the dataset using Python libraries (`pandas`).
- Cleaned data by handling missing values and inconsistencies.
- Identified key columns:
  - Product IDs
  - Stock levels
  - Sales data
  - Order dates

### Designing the SQL Database
The project database consists of the following tables:

1️⃣ Customers (customerID, customerName, phone, address, city, country)
Stores customer details.
2️⃣ Orders (orderNumber, orderDate, status, customerID)
Tracks each order and its customer.
3️⃣ Products (productCode, productLine, MSRP)
Stores product-related details.
4️⃣ OrderDetails (orderNumber, productCode, quantityOrdered, priceEach, sales)

