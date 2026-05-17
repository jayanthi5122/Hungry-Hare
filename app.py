from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("food_order.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    conn = get_db_connection()
    products = conn.execute("SELECT * FROM products").fetchall()
    conn.close()

    return render_template("index.html", products=products)


@app.route("/category/<category_name>")
def category(category_name):

    menu_items = {
        "burger": [
            {
                "name": "Classic Burger",
                "price": 8.99,
                "image": "images/classic_burger.jpg",
                "description": "Juicy grilled burger with fresh lettuce and sauce."
            },
            {
                "name": "Cheese Burger",
                "price": 9.99,
                "image": "images/cheese_burger.jpg",
                "description": "Loaded with melted cheese and crispy toppings."
            },
            {
                "name": "Chicken Burger",
                "price": 8.49,
                "image": "images/chicken_burger.jpg",
                "description": "Crispy chicken fillet with creamy mayo."
            },
            {
                "name": "Veggie Burger",
                "price": 7.99,
                "image": "images/veggie_burger.jpg",
                "description": "Fresh vegetable patty with healthy toppings."
            }
        ],

        "pizza": [
            {
                "name": "Pepperoni Pizza",
                "price": 12.99,
                "image": "images/pepperoni_pizza.jpg",
                "description": "Classic pepperoni pizza with mozzarella cheese."
            },
            {
                "name": "Veg Pizza",
                "price": 10.99,
                "image": "images/veg_pizza.jpg",
                "description": "Loaded with fresh vegetables and cheese."
            },
            {
                "name": "BBQ Chicken Pizza",
                "price": 13.99,
                "image": "images/bbq_chicken_pizza.jpg",
                "description": "BBQ chicken, onions, cheese, and smoky sauce."
            }
        ],

        "pasta": [
            {
                "name": "White Sauce Pasta",
                "price": 11.99,
                "image": "images/white_pasta.jpg",
                "description": "Creamy pasta with herbs and parmesan."
            },
            {
                "name": "Red Sauce Pasta",
                "price": 10.99,
                "image": "images/red_pasta.jpg",
                "description": "Tangy tomato pasta with Italian seasoning."
            }
        ],

        "fries": [
            {
                "name": "Classic Fries",
                "price": 4.99,
                "image": "images/classic_fries.jpg",
                "description": "Crispy golden fries with ketchup."
            },
            {
                "name": "Cheesy Fries",
                "price": 5.99,
                "image": "images/cheesy_fries.jpg",
                "description": "Fries loaded with melted cheese."
            }
        ],

        "sandwich": [
            {
                "name": "Club Sandwich",
                "price": 6.59,
                "image": "images/club_sandwich.jpg",
                "description": "Triple-layer sandwich with chicken and veggies."
            },
            {
                "name": "Grilled Cheese Sandwich",
                "price": 5.99,
                "image": "images/grilled_cheese.jpg",
                "description": "Toasted sandwich with melted cheese."
            }
        ],

        "dessert": [
            {
                "name": "Chocolate Cake",
                "price": 4.33,
                "image": "images/chocolate_cake.jpg",
                "description": "Rich chocolate cake slice."
            },
            {
                "name": "Ice Cream Sundae",
                "price": 4.99,
                "image": "images/icecream_sundae.jpg",
                "description": "Vanilla ice cream with chocolate syrup."
            }
        ],

        "coffee": [
            {
                "name": "Americano",
                "price": 2.69,
                "image": "images/americano.jpg",
                "description": "Fresh hot black coffee."
            },
            {
                "name": "Cappuccino",
                "price": 3.49,
                "image": "images/cappuccino.jpg",
                "description": "Espresso with steamed milk and foam."
            }
        ],

        "latte": [
            {
                "name": "Classic Latte",
                "price": 3.45,
                "image": "images/classic_latte.jpg",
                "description": "Smooth espresso with creamy milk."
            },
            {
                "name": "Caramel Latte",
                "price": 4.25,
                "image": "images/caramel_latte.jpg",
                "description": "Latte with sweet caramel flavour."
            }
        ],

        "chicken nuggets": [
            {
                "name": "6 Piece Nuggets",
                "price": 5.99,
                "image": "images/nuggets_6.jpg",
                "description": "Crispy chicken nuggets with dip."
            },
            {
                "name": "12 Piece Nuggets",
                "price": 9.99,
                "image": "images/nuggets_12.jpg",
                "description": "Perfect sharing box of nuggets."
            }
        ],

        "briyani": [
            {
                "name": "Chicken Biryani",
                "price": 12.99,
                "image": "images/chicken_biryani.jpg",
                "description": "Spicy aromatic rice with chicken."
            },
            {
                "name": "Veg Biryani",
                "price": 10.99,
                "image": "images/veg_biryani.jpg",
                "description": "Flavourful vegetable biryani."
            }
        ]
    }

    items = menu_items.get(category_name.lower(), [])

    return render_template(
        "category.html",
        category_name=category_name,
        items=items
    )

@app.route("/careers")
def careers():
    return render_template("careers.html")

@app.route("/payment")
def payment():
    return render_template("payment.html")

if __name__ == "__main__":
    app.run(debug=True)