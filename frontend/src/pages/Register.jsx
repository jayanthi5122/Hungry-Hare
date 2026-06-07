import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

function Register() {
  const [form, setForm] = useState({
    name: "",
    email: "",
    password: "",
  });

  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const navigate = useNavigate();

  async function handleRegister(e) {
    e.preventDefault();

    setMessage("");
    setError("");

    try {
      const response = await fetch("http://127.0.0.1:5001/api/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "include",
        body: JSON.stringify(form),
      });

      const data = await response.json();

      if (response.ok) {
        setMessage("Registration successful! Redirecting to login...");

        setTimeout(() => {
          navigate("/login");
        }, 1500);
      } else {
        setError(data.error || "Registration failed");
      }
    } catch (err) {
      setError("Backend server is not running.");
    }
  }

  return (
    <div className="min-h-screen bg-orange-50 flex items-center justify-center px-6">
      <div className="bg-white p-8 rounded-3xl shadow-xl w-full max-w-md">

        <h1 className="text-4xl font-bold text-orange-600 text-center mb-2">
          Hungry Hare 🍔
        </h1>

        <p className="text-center text-gray-500 mb-8">
          Create your account
        </p>

        {message && (
          <p className="bg-green-100 text-green-700 p-3 rounded-xl mb-4 text-center">
            {message}
          </p>
        )}

        {error && (
          <p className="bg-red-100 text-red-700 p-3 rounded-xl mb-4 text-center">
            {error}
          </p>
        )}

        <form onSubmit={handleRegister} className="space-y-5">

          <input
            type="text"
            placeholder="Full Name"
            required
            className="w-full bg-gray-100 p-4 rounded-xl focus:outline-none focus:ring-2 focus:ring-orange-500"
            value={form.name}
            onChange={(e) =>
              setForm({ ...form, name: e.target.value })
            }
          />

          <input
            type="email"
            placeholder="Email address"
            required
            className="w-full bg-gray-100 p-4 rounded-xl focus:outline-none focus:ring-2 focus:ring-orange-500"
            value={form.email}
            onChange={(e) =>
              setForm({ ...form, email: e.target.value })
            }
          />

          <input
            type="password"
            placeholder="Password"
            required
            className="w-full bg-gray-100 p-4 rounded-xl focus:outline-none focus:ring-2 focus:ring-orange-500"
            value={form.password}
            onChange={(e) =>
              setForm({ ...form, password: e.target.value })
            }
          />

          <button
            type="submit"
            className="w-full bg-black hover:bg-orange-600 text-white py-4 rounded-full font-bold text-lg transition"
          >
            Register
          </button>
        </form>

        <p className="text-center mt-6 text-gray-600">
          Already have an account?{" "}
          <Link to="/login" className="text-orange-600 font-bold">
            Login
          </Link>
        </p>

      </div>
    </div>
  );
}

export default Register;