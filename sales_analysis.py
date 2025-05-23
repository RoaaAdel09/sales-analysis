# -*- coding: utf-8 -*-
"""sales_analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rD1jKmNDHFVVAPMy-ujOOP85F4dtC1L2
"""

# This script performs an analysis of sales data, including:
# 1. Identifying the top-selling products.
# 2. Analyzing product profitability by comparing total sales with quantities sold.
# 3. Categorizing products into price ranges (Low, Medium, High) and analyzing sales by each price category.
#
# The script uses data provided in a CSV file and visualizes the results through various bar charts.
# It helps to uncover insights such as:
# - Which products are the highest performers in terms of sales.
# - How profitable each product is in relation to its sales volume.
# - How sales vary across different price categories.
#
# Required Libraries:
# - pandas: For data manipulation and analysis.
# - matplotlib: For generating visualizations.
#  Written by Roaa alfaqih


import pandas as pd
import matplotlib.pyplot as plt

# Load data from a CSV file
file_path = '/content/novatech_sales_data_large.csv'
data = pd.read_csv(file_path)

# Display the first 5 rows of the data
data.head()

missing_values = data.isnull().sum()
print(missing_values)

# Convert OrderDate to datetime format for time-based analysis
data['OrderDate'] = pd.to_datetime(data['OrderDate'])

# Calculate Total Sales for each order
data['Total_Sales'] = data['Price'] * data['Quantity']

#Analyze total sales by product category
category_sales = data.groupby('Category')['Total_Sales'].sum().sort_values(ascending=False)

#Analyze total sales by country
country_sales = data.groupby('Country')['Total_Sales'].sum().sort_values(ascending=False)

#Analyze sales trends by month
data['Month'] = data['OrderDate'].dt.to_period('M')
monthly_sales = data.groupby('Month')['Total_Sales'].sum()

#Analyze the top-selling products
top_selling_products = data.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)

#Analyze product profitability
product_profitability = data.groupby('Product').agg(
    Total_Sales=('Total_Sales', 'sum'),
    Total_Quantity=('Quantity', 'sum')
).sort_values(by='Total_Sales', ascending=False)

#Classify products into different price categories
price_bins = [0, 100, 200, 500]  # Define the price ranges
price_labels = ['Low', 'Medium', 'High']  # Labels for price categories
data['Price_Category'] = pd.cut(data['Price'], bins=price_bins, labels=price_labels, right=False)

#Analyze sales by price category
sales_by_price_category = data.groupby('Price_Category')['Total_Sales'].sum()

# Bar chart for Top Selling Products
plt.figure(figsize=(8, 6))
top_selling_products.head(10).plot(kind='bar', color='skyblue')
plt.title('Top Selling Products')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Bar chart for Product Profitability
plt.figure(figsize=(8, 6))
product_profitability.head(10)['Total_Sales'].plot(kind='bar', color='lightgreen')
plt.title('Product Profitability')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bar chart for Sales by Price Category
plt.figure(figsize=(8, 6))
sales_by_price_category.plot(kind='bar', color='orange')
plt.title('Sales by Price Category')
plt.xlabel('Price Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Plot for Sales by Category
plt.figure(figsize=(8, 6))
category_sales.plot(kind='bar', color='skyblue')
plt.title('Sales Analysis by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot for Sales by Country
plt.figure(figsize=(8, 6))
country_sales.plot(kind='bar', color='lightgreen')
plt.title('Sales Analysis by Country')
plt.xlabel('Country')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
monthly_sales.plot(kind='line', marker='o', color='orange')
plt.title('Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()
