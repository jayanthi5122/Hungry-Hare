import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jayanthi@5122",
    database="hungry_hare"
)

cursor = conn.cursor()

cursor.execute("DELETE FROM products")

foods = [
    ("Burger", 8.99, "images/burger.jpg"),
    ("Pizza", 12.59, "images/pizza.jpg"),
    ("Pasta", 10.99, "images/pasta.jpg"),
    ("Fries", 4.99, "images/fries.jpg"),
    ("Sandwich", 6.59, "images/sandwich.jpg"),
    ("Dessert", 4.33, "images/dessert.jpg"),
    ("Coffee", 2.69, "images/coffee.jpg"),
    ("Latte", 3.45, "images/latte.jpg"),
    ("Chicken Nuggets", 5.99, "images/chicken_nuggets.jpg"),
    ("Biryani", 12.99, "images/biryani.jpg")
]

cursor.executemany("""
INSERT INTO products(name, price, image)
VALUES (%s, %s, %s)
""", foods)

conn.commit()
cursor.close()
conn.close()

print("Products inserted into MySQL!")