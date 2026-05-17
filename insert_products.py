import sqlite3

conn = sqlite3.connect("food_order.db")
cursor = conn.cursor()

foods = [
    ("Burger", 8.99, "images/burger.jpg"),
    ("Pizza", 12.59, "images/pizza.jpg"),
    ("pasta", 10.99,"images/pasta.jpg"),
    ("fries", 4.99,"images/fries.jpg"),
    ("sandwich", 6.59,"images/sandwich.jpg"),
    ("dessert", 4.33,"images/dessert.jpg"),
    ("coffee",2.69,"images/coffee.jpg"),
    ("latte",3.45,"images/latte.jpg"),
    ("chicken nuggets",5.99,"images/chicken_nuggets.jpg"),
    ("Briyani",12.99, "images/biryani.jpg")
]
cursor.executemany("""
INSERT INTO products(name, price, image)
VALUES (?, ?, ?)
""", foods)

conn.commit()
conn.close()

print("Products inserted!")