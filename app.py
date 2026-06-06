from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import mysql.connector

app = Flask(__name__)
app.secret_key = "hungry_hare_secret_key"


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jayanthi@5122",
        database="hungry_hare"
    )


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))

        if session.get("role") != "admin":
            return "Access denied. Admins only."

        return f(*args, **kwargs)

    return decorated_function


@app.route("/")
def landing():
    if "user_id" in session:
        return redirect(url_for("home"))
    return redirect(url_for("login"))


@app.route("/home")
@login_required
def home():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("index.html", products=products)


@app.route("/category/<category_name>")
@login_required
def category(category_name):
    menu_items = {
        "burger": [
            {"name": "Classic Burger", "price": 8.99, "image": "images/classic_burger.jpg", "description": "Juicy grilled burger with fresh lettuce."},
            {"name": "Cheese Burger", "price": 9.99, "image": "images/cheese_burger.jpg", "description": "Loaded with melted cheese."},
            {"name": "Chicken Burger", "price": 8.49, "image": "images/chicken_burger.jpg", "description": "Crispy chicken fillet burger."},
            {"name": "Classic Veg Burger", "price": 6.97, "image": "images/veggie_burger.jpg", "description": "Loaded with veggies."}
        ],
        "pizza": [
            {"name": "Pepperoni Pizza", "price": 12.99, "image": "images/pepperoni_pizza.jpg", "description": "Classic pepperoni pizza."},
            {"name": "Veg Pizza", "price": 10.99, "image": "images/veg_pizza.jpg", "description": "Fresh vegetable toppings."},
            {"name": "BBQ Chicken Pizza", "price": 13.20, "image": "images/bbq_chicken_pizza.jpg", "description": "Smokey BBQ pizza."}
        ],
        "pasta": [
            {"name": "White Sauce Pasta", "price": 11.99, "image": "images/white_pasta.jpg", "description": "Creamy Italian pasta."},
            {"name": "Red Sauce Pasta", "price": 10.99, "image": "images/red_pasta.jpg", "description": "Tomato pasta with herbs."}
        ],
        "fries": [
            {"name": "Classic Fries", "price": 4.99, "image": "images/classic_fries.jpg", "description": "Crispy golden fries."},
            {"name": "Cheesy Fries", "price": 5.99, "image": "images/cheesy_fries.jpg", "description": "Fries with melted cheese."}
        ],
        "sandwich": [
            {"name": "Club Sandwich", "price": 6.59, "image": "images/club_sandwich.jpg", "description": "Chicken club sandwich."}
        ],
        "dessert": [
            {"name": "Chocolate Cake", "price": 4.33, "image": "images/chocolate_cake.jpg", "description": "Rich chocolate cake."},
            {"name": "Ice Cream Sundae", "price": 5.39, "image": "images/icecream_sundae.jpg", "description": "Creamy sundae."}
        ],
        "coffee": [
            {"name": "Americano", "price": 2.69, "image": "images/americano.jpg", "description": "Fresh black coffee."},
            {"name": "Cappuccino", "price": 3.20, "image": "images/cappuccino.jpg", "description": "Fresh milk cappuccino."}
        ],
        "latte": [
            {"name": "Classic Latte", "price": 3.45, "image": "images/classic_latte.jpg", "description": "Smooth creamy latte."},
            {"name": "Caramel Latte", "price": 4.55, "image": "images/caramel_latte.jpg", "description": "Smooth caramel latte."}
        ],
        "chicken nuggets": [
            {"name": "6 Piece Nuggets", "price": 5.99, "image": "images/nuggets_6.jpg", "description": "Crispy chicken nuggets."},
            {"name": "12 Piece Nuggets", "price": 11.99, "image": "images/nuggets_12.jpg", "description": "Crispy chicken nuggets."}
        ],
        "biryani": [
            {"name": "Veggie Biryani", "price": 11.99, "image": "images/veg_biryani.jpg", "description": "Veggie biryani."},
            {"name": "Chicken Biryani", "price": 12.99, "image": "images/chicken_biryani.jpg", "description": "Spicy chicken biryani."}
        ]
    }

    items = menu_items.get(category_name.lower(), [])
    return render_template("category.html", category_name=category_name, items=items)


@app.route("/register", methods=["GET", "POST"])
def register():
    if "user_id" in session:
        return redirect(url_for("home"))

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute(
                "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                (name, email, hashed_password)
            )
            conn.commit()
        except mysql.connector.IntegrityError:
            cursor.close()
            conn.close()
            return "Email already registered!"

        cursor.close()
        conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if "user_id" in session:
        return redirect(url_for("home"))

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM users WHERE email = %s",
            (email,)
        )

        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            session["user_name"] = user["name"]
            session["role"] = user["role"]
            return redirect(url_for("home"))

        return "Invalid email or password!"

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/checkout", methods=["POST"])
@login_required
def checkout():
    data = request.get_json()

    cart = data.get("cart", [])
    total = data.get("total", 0)

    if not cart:
        return jsonify({"error": "Cart is empty"}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "INSERT INTO orders (user_id, customer_name, total, status) VALUES (%s, %s, %s, %s)",
        (session["user_id"], session["user_name"], total, "Confirmed")
    )

    order_id = cursor.lastrowid

    for item in cart:
        cursor.execute(
            "INSERT INTO order_items (order_id, item_name, price, quantity) VALUES (%s, %s, %s, %s)",
            (
                order_id,
                item["name"],
                item["price"],
                item.get("quantity", 1)
            )
        )

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "message": "Order placed successfully!",
        "order_id": order_id
    })


@app.route("/order-confirmation/<int:order_id>")
@login_required
def order_confirmation(order_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM orders WHERE id = %s AND user_id = %s",
        (order_id, session["user_id"])
    )
    order = cursor.fetchone()

    cursor.execute(
        "SELECT * FROM order_items WHERE order_id = %s",
        (order_id,)
    )
    items = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "order_confirmation.html",
        order=order,
        items=items
    )


@app.route("/order-history")
@login_required
def order_history():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM orders WHERE user_id = %s ORDER BY created_at DESC",
        (session["user_id"],)
    )

    orders = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("order_history.html", orders=orders)


@app.route("/payment")
@login_required
def payment():
    return render_template("payment.html")


@app.route("/careers")
@login_required
def careers():
    return render_template("careers.html")

@app.route("/admin")
@admin_required
def admin_dashboard():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    cursor.execute("SELECT * FROM orders ORDER BY created_at DESC")
    orders = cursor.fetchall()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "admin_dashboard.html",
        users=users,
        orders=orders,
        products=products
    )
    
@app.route("/admin/add-product", methods=["GET", "POST"])
@admin_required
def add_product():
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        image = request.form["image"]

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO products (name, price, image) VALUES (%s, %s, %s)",
            (name, price, image)
        )

        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for("admin_dashboard"))

    return render_template("add_product.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)