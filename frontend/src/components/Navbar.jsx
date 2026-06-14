import { Link, useNavigate } from "react-router-dom";

function Navbar() {
  const navigate = useNavigate();

  async function logout() {
    await fetch("http://13.218.89.254:5001/api/logout", {
      method: "POST",
      credentials: "include",
    });

    navigate("/login");
  }

  return (
    <nav className="bg-white shadow-md px-6 py-4 flex justify-between items-center sticky top-0 z-50">
      <Link to="/home" className="text-3xl font-bold text-orange-600">
        Hungry Hare 🍔
      </Link>

      <div className="flex gap-5 font-semibold">
        <Link to="/home">Home</Link>
        <Link to="/cart">Cart</Link>
        <Link to="/orders">Orders</Link>
        <Link to="/payment">Payment</Link>
        <Link to="/location">Location</Link>
        <button onClick={logout} className="text-red-600">
          Logout
        </button>
      </div>
    </nav>
  );
}

export default Navbar;