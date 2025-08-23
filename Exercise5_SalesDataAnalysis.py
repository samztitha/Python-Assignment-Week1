import pandas as pd

try:
    # Read CSV file
    df = pd.read_csv("sales_data.csv")

    # Calculate total sales
    df["Total_Sales"] = df["Quantity"] * df["Price"]

    # Top 3 products by sales
    top_products = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False).head(3)
    print("\nTop 3 Products:\n", top_products)

    # Revenue per product
    revenue = df.groupby("Product")["Total_Sales"].sum()
    print("\nRevenue per product:\n", revenue)

    # Highest sales day
    highest_day = df.groupby("Date")["Total_Sales"].sum().idxmax()
    print("\nHighest sales day:", highest_day)

    # Plot bar chart
    revenue.plot(kind="bar", title="Product-wise Revenue")

except FileNotFoundError:
    print(" Sales data file not found. Please check filename.")
except Exception as e:
    print(" Error:", e)
