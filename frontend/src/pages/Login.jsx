import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const navigate = useNavigate();

  async function handleLogin(e) {
    e.preventDefault();

    const response = await fetch("http://13.218.89.254:5001/api/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include",
      body: JSON.stringify({ email, password }),
    });

    const data = await response.json();

    if (response.ok) {
    localStorage.setItem("hungryHareUser", JSON.stringify(data.user));
      navigate("/home");
    } else {
      setError(data.error || "Login failed");
    }
  }

  return (
    <div className="min-h-screen bg-[#f6f6f6] flex items-center justify-center px-6">
      <div className="w-full max-w-md bg-white rounded-3xl shadow-xl p-8">

        <h1 className="text-4xl font-bold text-center text-orange-600 mb-2">
          Hungry Hare 🍔
        </h1>

        <p className="text-center text-gray-500 mb-8">
          Login to order your favourite food
        </p>

        {error && (
          <p className="bg-red-100 text-red-600 p-3 rounded-xl mb-4 text-center">
            {error}
          </p>
        )}

        <form onSubmit={handleLogin} className="space-y-5" autocomplete="off">

          <input
  type="text"
  name="hungryhare-login-email"
  placeholder="Email address"
  autoComplete="new-password"
  className="w-full bg-gray-100 border-none p-4 rounded-xl focus:outline-none focus:ring-2 focus:ring-orange-500"
  value={email}
  onChange={(e) => setEmail(e.target.value)}
/>

          <input
  type="password"
  name="hungryhare-login-password"
  placeholder="Password"
  autoComplete="new-password"
  className="w-full bg-gray-100 border-none p-4 rounded-xl focus:outline-none focus:ring-2 focus:ring-orange-500"
  value={password}
  onChange={(e) => setPassword(e.target.value)}
/>

          <button
            type="submit"
            className="w-full bg-black hover:bg-orange-600 text-white py-4 rounded-full font-bold text-lg transition"
          >
            Login
          </button>
          <div className="text-right">
  <a
  href="mailto:support@hungryhare.com?subject=Password Recovery Request"
  className="text-sm text-orange-600 font-bold hover:underline"
>
  Forgot username or password?
</a>
</div>

        </form>

        <p className="text-center mt-6 text-gray-600">
          New user?{" "}
          <Link to="/register" className="text-orange-600 font-bold">
            Create account
          </Link>
        </p>

      </div>
    </div>
  );
}

export default Login;