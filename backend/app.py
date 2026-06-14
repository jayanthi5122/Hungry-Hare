from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = "hungry_hare_secret_key"

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "your_email@gmail.com"
app.config["MAIL_PASSWORD"] = "your_gmail_app_password"

mail = Mail(app)
serializer = URLSafeTimedSerializer(app.secret_key)

CORS(
    app,
    supports_credentials=True,
    resources={
        r"/api/*": {
            "origins": [
                "http://127.0.0.1:5173",
                "http://localhost:5173",
                "http://13.218.89.254:5173"
            ]
        }
    }
)

app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["SESSION_COOKIE_SECURE"] = False

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", "Jayanthi@5122"),
        database=os.getenv("MYSQL_DATABASE", "hungry_hare")
    )


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return jsonify({"error": "Login required"}), 401
        return f(*args, **kwargs)
    return decorated_function


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return jsonify({"error": "Login required"}), 401

        if session.get("role") != "admin":
            return jsonify({"error": "Admins only"}), 403

        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
def index():
    return jsonify({"message": "Hungry Hare Flask API is running"})


@app.route("/api/products", methods=["GET"])
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(products)


@app.route("/api/category/<category_name>", methods=["GET"])
def get_category_items(category_name):
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
    
    category_key = category_name.lower().strip()
    items = menu_items.get(category_name.lower(), [])

    return jsonify({
        "category": category_name,
        "items": items
    })


@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({"error": "Name, email and password are required"}), 400

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
        return jsonify({"error": "Email already registered"}), 400

    cursor.close()
    conn.close()

    return jsonify({"message": "Registered successfully"}), 201


@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

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

        return jsonify({
            "message": "Login successful",
            "user": {
                "id": user["id"],
                "name": user["name"],
                "email": user["email"],
                "role": user["role"]
            }
        })

    return jsonify({"error": "Invalid email or password"}), 401


@app.route("/api/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully"})


@app.route("/api/me", methods=["GET"])
def me():
    if "user_id" not in session:
        return jsonify({"logged_in": False}), 200

    return jsonify({
        "logged_in": True,
        "user": {
            "id": session["user_id"],
            "name": session["user_name"],
            "role": session["role"]
        }
    })


@app.route("/api/checkout", methods=["POST"])
def checkout():
    data = request.get_json()

    cart = data.get("cart", [])
    total = data.get("total", 0)
    user_id = data.get("user_id")
    customer_name = data.get("customer_name", "Guest")

    if not cart:
        return jsonify({"error": "Cart is empty"}), 400

    if not user_id:
        return jsonify({"error": "User missing. Please login again."}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "INSERT INTO orders (user_id, customer_name, total, status) VALUES (%s, %s, %s, %s)",
        (user_id, customer_name, total, "Confirmed")
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
        "message": "Order placed successfully",
        "order_id": order_id
    })


@app.route("/api/orders", methods=["GET"])
def order_history():
    user_id = request.args.get("user_id")

    if not user_id:
        return jsonify([])

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM orders WHERE user_id = %s ORDER BY created_at DESC",
        (user_id,)
    )

    orders = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(orders)


@app.route("/api/orders/<int:order_id>", methods=["GET"])
@login_required
def order_details(order_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM orders WHERE id = %s AND user_id = %s",
        (order_id, session["user_id"])
    )
    order = cursor.fetchone()

    if not order:
        cursor.close()
        conn.close()
        return jsonify({"error": "Order not found"}), 404

    cursor.execute(
        "SELECT * FROM order_items WHERE order_id = %s",
        (order_id,)
    )
    items = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify({
        "order": order,
        "items": items
    })


@app.route("/api/admin/dashboard", methods=["GET"])
def admin_dashboard():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, name, email, role FROM users")
    users = cursor.fetchall()

    cursor.execute("SELECT * FROM orders ORDER BY created_at DESC")
    orders = cursor.fetchall()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify({
        "users": users,
        "orders": orders,
        "products": products
    })


@app.route("/api/admin/products", methods=["POST"])
@admin_required
def add_product():
    data = request.get_json()

    name = data.get("name")
    price = data.get("price")
    image = data.get("image")

    if not name or not price or not image:
        return jsonify({"error": "Name, price and image are required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "INSERT INTO products (name, price, image) VALUES (%s, %s, %s)",
        (name, price, image)
    )

    conn.commit()
    product_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return jsonify({
        "message": "Product added successfully",
        "product_id": product_id
    }), 201
    
    
@app.route("/api/forgot-password", methods=["POST"])
def forgot_password():
    data = request.get_json()
    email = data.get("email")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if not user:
        return jsonify({"error": "Email not found"}), 404

    token = serializer.dumps(email, salt="password-reset-salt")

    reset_link = f"http://127.0.0.1:5173/reset-password/{token}"

    msg = Message(
        "Hungry Hare Password Reset",
        sender=app.config["MAIL_USERNAME"],
        recipients=[email]
    )

    msg.body = f"""
Hello {user['name']},

Click the link below to reset your Hungry Hare password:

{reset_link}

This link will expire in 30 minutes.

If you did not request this, please ignore this email.
"""

    mail.send(msg)

    return jsonify({"message": "Password reset link sent to your email"})


@app.route("/api/reset-password/<token>", methods=["POST"])
def reset_password(token):
    data = request.get_json()
    new_password = data.get("password")

    try:
        email = serializer.loads(
            token,
            salt="password-reset-salt",
            max_age=1800
        )
    except:
        return jsonify({"error": "Invalid or expired reset link"}), 400

    hashed_password = generate_password_hash(new_password)

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET password = %s WHERE email = %s",
        (hashed_password, email)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Password reset successful"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
