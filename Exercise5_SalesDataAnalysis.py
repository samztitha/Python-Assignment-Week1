# Exercise 5: Sales Data Analysis
# Author: Samztitha
# Reads sales data from CSV and gives basic analysis.

import pandas as pd

try:
    # Step 1: Load sales data
    file_name = "sales_data.csv"
    data = pd.read_csv(file_name)

    print("\n=== Sales Data Preview ===")
    print(data.head(), "\n")

    # Step 2: Total sales
    total_sales = data["Sales"].sum()
    print(f" Total Sales: {total_sales}")

    # Step 3: Average sales
    avg_sales = data["Sales"].mean()
    print(f" Average Sales: {avg_sales:.2f}")

    # Step 4: Highest and lowest
    max_sale = data.loc[data["Sales"].idxmax()]
    min_sale = data.loc[data["Sales"].idxmin()]
    print(f" Highest Sale: {max_sale['Sales']} (Product: {max_sale['Product']})")
    print(f"Lowest Sale: {min_sale['Sales']} (Product: {min_sale['Product']})")

except FileNotFoundError:
    print(f" File '{file_name}' not found. Please check the location.")
except Exception as e:
    print("Error occurred:", e)

