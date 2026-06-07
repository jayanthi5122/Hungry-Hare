import { useEffect, useState } from "react";
import Navbar from "../components/Navbar.jsx";

function OrderHistory() {
  const [orders, setOrders] = useState([]);
  const [error, setError] = useState("");

 useEffect(() => {
  const user = JSON.parse(localStorage.getItem("hungryHareUser"));

  if (!user) {
    setError("Please login to view your orders.");
    return;
  }

  fetch(`http://127.0.0.1:5001/api/orders?user_id=${user.id}`)
    .then((res) => res.json())
    .then((data) => setOrders(data))
    .catch(() => setError("Could not load orders."));
}, []);

  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />

      <section className="max-w-5xl mx-auto px-6 py-12">
        <h1 className="text-5xl font-bold text-orange-600 mb-8">
          Order History 📦
        </h1>

        {error && (
          <div className="bg-red-100 text-red-700 p-5 rounded-2xl mb-6">
            {error}
          </div>
        )}

        {orders.length === 0 && !error ? (
          <div className="bg-white rounded-3xl shadow-lg p-10 text-center">
            <p className="text-xl text-gray-500">
              No orders yet.
            </p>
          </div>
        ) : (
          <div className="space-y-6">
            {orders.map((order) => (
              <div
                key={order.id}
                className="bg-white rounded-3xl shadow-lg p-6"
              >
                <div className="flex flex-col md:flex-row md:justify-between md:items-center gap-4">
                  <div>
                    <h2 className="text-2xl font-bold">
                      Order #{order.id}
                    </h2>

                    <p className="text-gray-500">
                      {order.created_at}
                    </p>
                  </div>

                  <div className="md:text-right">
                    <p className="text-green-600 font-bold">
                      {order.status}
                    </p>

                    <p className="text-2xl font-bold text-orange-600">
                      € {Number(order.total).toFixed(2)}
                    </p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </section>
    </div>
  );
}

export default OrderHistory;