import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import Navbar from "../components/Navbar";

function Home() {
  const [products, setProducts] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:5001/api/products", {
      credentials: "include",
    })
      .then((res) => res.json())
      .then((data) => setProducts(data));
  }, []);

  const filtered = products.filter((p) =>
    p.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="bg-gray-100 min-h-screen">
      <Navbar />

      <section className="bg-white px-6 py-10">
        <p className="text-gray-500 mb-2">Deliver now</p>

        <input
          type="text"
          placeholder="Enter delivery location"
          className="w-full md:w-1/2 bg-gray-100 p-4 rounded-full mb-5"
        />

        <input
          type="text"
          placeholder="Search food..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="w-full bg-gray-100 p-4 rounded-full"
        />
      </section>

      <section className="px-6 py-10">
        <h2 className="text-4xl font-bold mb-8">Food Categories</h2>

        {filtered.length === 0 ? (
  <div className="bg-white rounded-3xl shadow-lg p-8 text-center col-span-full">
    <h2 className="text-3xl font-bold text-red-500 mb-3">
      😔 Sorry!
    </h2>

    <p className="text-gray-600">
      "{search}" is currently not available.
    </p>

    <p className="text-gray-500 mt-2">
      Please try another delicious option from our menu.
    </p>
  </div>
) : (
  <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
    {filtered.map((product) => (
      <Link
        key={product.id}
        to={`/category/${product.name}`}
        className="bg-white rounded-3xl shadow-lg overflow-hidden hover:-translate-y-2 transition"
      >
        <img
          src={`http://127.0.0.1:5001/static/${product.image}`}
          className="w-full h-52 object-cover"
        />

        <div className="p-5">
          <h3 className="text-2xl font-bold">{product.name}</h3>
          <p className="text-gray-500">Explore {product.name}</p>
        </div>
      </Link>
    ))}
  </div>
)}
      </section>
      <footer className="bg-grey text-darkblue py-4 mt-16">
  <div className="text-center text-sm md:text-base">
    Customer Care: +353 89 123 4567 |
    Careers |
    Location: Dublin, Ireland |
    Email: support@hungryhare.com
  </div>
</footer>
    </div>
  );
}

export default Home;