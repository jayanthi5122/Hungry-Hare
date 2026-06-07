import { Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login.jsx";
import Register from "./pages/Register.jsx";
import Home from "./pages/Home.jsx";
import Category from "./pages/Category.jsx";
import Cart from "./pages/Cart.jsx";
import OrderHistory from "./pages/OrderHistory.jsx";
import Payment from "./pages/Payment.jsx";
import Location from "./pages/Location.jsx";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/login" />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/home" element={<Home />} />
      <Route path="/category/:categoryName" element={<Category />} />
      <Route path="/cart" element={<Cart />} />
      <Route path="/orders" element={<OrderHistory />} />
      <Route path="/payment" element={<Payment />} />
      <Route path="/location" element={<Location />} />
    </Routes>
  );
}

export default App;