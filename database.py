import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('insights.db')

# Load CSV dataset
sales_data = pd.read_csv('../data/sales_data.csv')

# Store data in SQL table
sales_data.to_sql('sales', conn, if_exists='replace', index=False)

print('Database created successfully!')

conn.close()
