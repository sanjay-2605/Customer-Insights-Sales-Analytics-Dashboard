import pandas as pd
import matplotlib.pyplot as plt

# Load data
sales_data = pd.read_csv('../data/sales_data.csv')

# Revenue by category
sales_data['Revenue'] = sales_data['Quantity'] * sales_data['Price']

category_revenue = sales_data.groupby('Category')['Revenue'].sum()

# Plot graph
plt.figure(figsize=(6, 6))
category_revenue.plot(kind='pie', autopct='%1.1f%%')
plt.title('Revenue Distribution by Category')
plt.ylabel('')
plt.show()
