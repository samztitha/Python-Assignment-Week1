import pandas as pd

# Create sample sales data
data = {
    "Date": [
        "2025-08-01", "2025-08-01", "2025-08-02",
        "2025-08-02", "2025-08-03", "2025-08-03",
        "2025-08-04", "2025-08-05"
    ],
    "Product": [
        "Pen", "Notebook", "Pencil",
        "Notebook", "Eraser", "Pen",
        "Notebook", "Pen"
    ],
    "Quantity": [10, 5, 20, 10, 15, 25, 8, 30],
    "Price": [5, 50, 2, 50, 3, 5, 50, 5],
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# Add a new column for total sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

# Top 3 products by total revenue
top3 = df.groupby("Product")["Total_Sales"].sum().nlargest(3)
print("Top 3 products by sales:\n", top3, "\n")

# Total revenue per product
revenue = df.groupby("Product")["Total_Sales"].sum()
print("Revenue per product:\n", revenue, "\n")

# Find the day with highest sales
best_day = df.groupby("Date")["Total_Sales"].sum().idxmax()
print("Highest sales day:", best_day)
