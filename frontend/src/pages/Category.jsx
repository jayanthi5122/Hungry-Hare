import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import Navbar from "../components/Navbar.jsx";

function Category() {
  const { categoryName } = useParams();
  const [items, setItems] = useState([]);
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch(`http://13.218.89.254:5001/api/category/${categoryName}`, {
      credentials: "include",
    })
      .then((res) => res.json())
      .then((data) => setItems(data.items || []))
      .catch((err) => console.log(err));
  }, [categoryName]);

  function addToCart(item) {
    const oldCart = JSON.parse(localStorage.getItem("hungryHareCart")) || [];

    const existingItem = oldCart.find((cartItem) => cartItem.name === item.name);

    let updatedCart;

    if (existingItem) {
      updatedCart = oldCart.map((cartItem) =>
        cartItem.name === item.name
          ? { ...cartItem, quantity: cartItem.quantity + 1 }
          : cartItem
      );
    } else {
      updatedCart = [...oldCart, { ...item, quantity: 1 }];
    }

    localStorage.setItem("hungryHareCart", JSON.stringify(updatedCart));
    setMessage(`${item.name} added to cart`);
  }

  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />

      <section className="bg-white px-6 py-10">
        <Link to="/home" className="text-orange-600 font-bold">
          ← Back to menu
        </Link>

        <h1 className="text-4xl md:text-6xl font-bold mt-6 capitalize">
          {categoryName} Menu
        </h1>

        <p className="text-gray-500 mt-3">
          Choose your favourite {categoryName} items
        </p>

        {message && (
          <p className="mt-5 bg-green-100 text-green-700 p-4 rounded-xl inline-block">
            {message}
          </p>
        )}
      </section>

      <section className="px-6 py-10">
        {items.length === 0 ? (
          <div className="bg-white rounded-3xl shadow-lg p-10 text-center">
            <h2 className="text-3xl font-bold text-gray-700">
              No items found
            </h2>
            <p className="text-gray-500 mt-3">
              No menu items available for this category yet.
            </p>
          </div>
        ) : (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
            {items.map((item) => (
              <div
                key={item.name}
                className="bg-white rounded-3xl shadow-lg overflow-hidden hover:-translate-y-2 transition"
              >
                <img
                  src={`http://13.218.89.254:5001/static/${item.image}`}
                  alt={item.name}
                  className="w-full h-56 object-cover"
                />

                <div className="p-5">
                  <h3 className="text-2xl font-bold text-gray-900">
                    {item.name}
                  </h3>

                  <p className="text-gray-500 mt-2 min-h-12">
                    {item.description}
                  </p>

                  <p className="text-xl font-bold mt-4">
                    € {Number(item.price).toFixed(2)}
                  </p>

                  <button
                    onClick={() => addToCart(item)}
                    className="w-full mt-5 bg-black hover:bg-orange-600 text-white py-3 rounded-full font-bold transition"
                  >
                    Add to Cart
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </section>
    </div>
  );
}

export default Category;