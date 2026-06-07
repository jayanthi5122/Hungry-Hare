import { useEffect, useState } from "react";
import Navbar from "../components/Navbar.jsx";
import { useNavigate } from "react-router-dom";

function Cart() {
  const [cart, setCart] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const savedCart = JSON.parse(localStorage.getItem("hungryHareCart")) || [];
    setCart(savedCart);
  }, []);

  function saveCart(updatedCart) {
    setCart(updatedCart);
    localStorage.setItem("hungryHareCart", JSON.stringify(updatedCart));
  }

  function increase(name) {
    const updated = cart.map((item) =>
      item.name === name ? { ...item, quantity: item.quantity + 1 } : item
    );
    saveCart(updated);
  }

  function decrease(name) {
    const updated = cart
      .map((item) =>
        item.name === name ? { ...item, quantity: item.quantity - 1 } : item
      )
      .filter((item) => item.quantity > 0);

    saveCart(updated);
  }

  function removeItem(name) {
    saveCart(cart.filter((item) => item.name !== name));
  }

  const total = cart.reduce(
    (sum, item) => sum + Number(item.price) * item.quantity,
    0
  );

  function checkout() {
    if (cart.length === 0) {
      alert("Your cart is empty");
      return;
    }
    navigate("/payment");
}

  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />

      <section className="max-w-4xl mx-auto px-6 py-10">
        <h1 className="text-5xl font-bold mb-8">Your Cart 🛒</h1>

        {cart.length === 0 ? (
          <div className="bg-white p-10 rounded-3xl shadow text-center">
            <p className="text-xl text-gray-500">Your cart is empty.</p>
          </div>
        ) : (
          <div className="space-y-5">
            {cart.map((item) => (
              <div
                key={item.name}
                className="bg-white rounded-3xl shadow p-5 flex flex-col md:flex-row md:items-center md:justify-between gap-5"
              >
                <div>
                  <h2 className="text-2xl font-bold">{item.name}</h2>
                  <p className="text-gray-500">
                    € {Number(item.price).toFixed(2)}
                  </p>
                </div>

                <div className="flex items-center gap-4">
                  <button
                    onClick={() => decrease(item.name)}
                    className="bg-gray-200 px-4 py-2 rounded-full font-bold"
                  >
                    -
                  </button>

                  <span className="text-xl font-bold">{item.quantity}</span>

                  <button
                    onClick={() => increase(item.name)}
                    className="bg-gray-200 px-4 py-2 rounded-full font-bold"
                  >
                    +
                  </button>

                  <button
                    onClick={() => removeItem(item.name)}
                    className="text-red-600 font-bold"
                  >
                    Remove
                  </button>
                </div>
              </div>
            ))}

            <div className="bg-white rounded-3xl shadow p-6">
              <div className="flex justify-between text-3xl font-bold mb-6">
                <span>Total</span>
                <span>€ {total.toFixed(2)}</span>
              </div>

              <button
                onClick={checkout}
                className="w-full bg-green-600 hover:bg-green-700 text-white py-4 rounded-full text-xl font-bold"
              >
                Checkout
              </button>
            </div>
          </div>
        )}
      </section>
    </div>
  );
}

export default Cart;