import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Display dataset
print("\nSales Dataset:")
print(df)

# Total Sales
total_sales = df['Sales'].sum()
print("\nTotal Sales:", total_sales)

# Total Profit
total_profit = df['Profit'].sum()
print("Total Profit:", total_profit)

# Product-wise Sales
product_sales = df.groupby('Product')['Sales'].sum()

print("\nProduct-wise Sales:")
print(product_sales)

# Region-wise Sales
region_sales = df.groupby('Region')['Sales'].sum()

print("\nRegion-wise Sales:")
print(region_sales)

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Monthly Sales Trend
df['Month'] = df['Date'].dt.month

monthly_sales = df.groupby('Month')['Sales'].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# Plot Product-wise Sales
plt.figure(figsize=(8,5))
product_sales.plot(kind='bar')

plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.grid(True)

plt.show()

# Plot Monthly Sales
plt.figure(figsize=(8,5))
monthly_sales.plot(marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)

plt.show()
