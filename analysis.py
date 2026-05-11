import sqlite3
import pandas as pd

conn = sqlite3.connect('insights.db')

# Total Revenue
query1 = """
SELECT SUM(Quantity * Price) AS TotalRevenue
FROM sales
"""

revenue = pd.read_sql_query(query1, conn)
print("Total Revenue")
print(revenue)

# Top Selling Products
query2 = """
SELECT Product, SUM(Quantity) AS TotalSold
FROM sales
GROUP BY Product
ORDER BY TotalSold DESC
"""

products = pd.read_sql_query(query2, conn)
print("\nTop Selling Products")
print(products)

# Category Revenue
query3 = """
SELECT Category, SUM(Quantity * Price) AS Revenue
FROM sales
GROUP BY Category
"""

categories = pd.read_sql_query(query3, conn)
print("\nCategory Revenue")
print(categories)

conn.close()
