USE ecommerce_inventory;


-- Customers Table
CREATE TABLE Customers (
    customerID INT AUTO_INCREMENT PRIMARY KEY,
    customerName VARCHAR(100),
    contactLastName VARCHAR(50),
    contactFirstName VARCHAR(50),
    phone VARCHAR(20),
    addressLine1 VARCHAR(255),
    city VARCHAR(50),
    state VARCHAR(50),
    postalCode VARCHAR(20),
    country VARCHAR(50)
);

-- Orders Table
CREATE TABLE Orders (
    orderNumber INT PRIMARY KEY,
    orderDate DATE,
    status VARCHAR(50),
    qtr_id INT,
    month_id INT,
    year_id INT,
    customerID INT,
    FOREIGN KEY (customerID) REFERENCES Customers(customerID)
);

-- Products Table
CREATE TABLE Products (
    productCode VARCHAR(50) PRIMARY KEY,
    productLine VARCHAR(100),
    MSRP DECIMAL(10,2)
);

-- OrderDetails Table
CREATE TABLE OrderDetails (
    orderNumber INT,
    productCode VARCHAR(50),
    quantityOrdered INT,
    priceEach DECIMAL(10,2),
    orderLineNumber INT,
    sales DECIMAL(10,2),
    PRIMARY KEY (orderNumber, productCode),
    FOREIGN KEY (orderNumber) REFERENCES Orders(orderNumber),
    FOREIGN KEY (productCode) REFERENCES Products(productCode)
);


