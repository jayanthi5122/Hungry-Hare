import { useState } from "react";
import { useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar.jsx";

function Payment() {
  const [paymentMethod, setPaymentMethod] = useState("cod");
  const navigate = useNavigate();

  async function handlePayment() {
    alert("Payment button clicked!");

    const cart = JSON.parse(localStorage.getItem("hungryHareCart")) || [];
    const user = JSON.parse(localStorage.getItem("hungryHareUser"));

    console.log("User:", user);
    console.log("Cart:", cart);

    if (!user) {
      alert("User not found. Please login again.");
      navigate("/login");
      return;
    }

    if (cart.length === 0) {
      alert("Your cart is empty.");
      navigate("/home");
      return;
    }

    const total = cart.reduce(
      (sum, item) => sum + Number(item.price) * item.quantity,
      0
    );

    try {
      const response = await fetch(
        "http://127.0.0.1:5001/api/checkout",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            cart,
            total,
            user_id: user.id,
            customer_name: user.name,
          }),
        }
      );

      const data = await response.json();

      console.log("Checkout response:", data);

      if (response.ok) {
        localStorage.removeItem("hungryHareCart");
        alert("Order placed successfully!");
        navigate("/orders");
      } else {
        alert(data.error || "Payment failed.");
      }
    } catch (error) {
      console.error(error);
      alert("Backend connection failed.");
    }
  }

  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />

      <section className="max-w-2xl mx-auto px-6 py-12">
        <div className="bg-white rounded-3xl shadow-xl p-8">
          <h1 className="text-4xl font-bold text-orange-600 text-center mb-3">
            Payment 💳
          </h1>

          <p className="text-gray-500 text-center mb-8">
            Choose your preferred payment method.
          </p>

          <div className="space-y-4 mb-8">
            <label className="flex items-center gap-4 bg-gray-100 p-4 rounded-2xl cursor-pointer">
              <input
                type="radio"
                name="payment"
                value="cod"
                checked={paymentMethod === "cod"}
                onChange={(e) => setPaymentMethod(e.target.value)}
              />
              <span className="font-bold">Cash on Delivery</span>
            </label>

            <label className="flex items-center gap-4 bg-gray-100 p-4 rounded-2xl cursor-pointer">
              <input
                type="radio"
                name="payment"
                value="card"
                checked={paymentMethod === "card"}
                onChange={(e) => setPaymentMethod(e.target.value)}
              />
              <span className="font-bold">Credit / Debit Card</span>
            </label>

            <label className="flex items-center gap-4 bg-gray-100 p-4 rounded-2xl cursor-pointer">
              <input
                type="radio"
                name="payment"
                value="wallet"
                checked={paymentMethod === "wallet"}
                onChange={(e) => setPaymentMethod(e.target.value)}
              />
              <span className="font-bold">PayPal / Digital Wallet</span>
            </label>
          </div>

          <button
            type="button"
            onClick={handlePayment}
            className="w-full bg-black hover:bg-orange-600 text-white py-4 rounded-full font-bold text-lg"
          >
            Confirm Payment
          </button>
        </div>
      </section>
    </div>
  );
}

export default Payment;