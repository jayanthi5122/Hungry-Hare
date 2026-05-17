import sqlite3

# connect to database
conn = sqlite3.connect("food_order.db")

# create cursor
cursor = conn.cursor()

# create products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    image TEXT
)
""")

# create orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    items TEXT,
    total REAL
)
""")

# save changes
conn.commit()

# close connection
conn.close()

print("Database created successfully!")