let cart = JSON.parse(localStorage.getItem("hungryHareCart")) || [];

function saveCart() {
    localStorage.setItem("hungryHareCart", JSON.stringify(cart));
}

function addToCart(name, price) {
    price = Number(price);

    cart.push({ name: name, price: price });

    saveCart();
    updateCart();
    openCart();
}

function updateCart() {
    const cartItems = document.getElementById("cart-items");
    const cartTotal = document.getElementById("cart-total");
    const cartCount = document.getElementById("cart-count");

    if (!cartItems || !cartTotal) return;

    cartItems.innerHTML = "";

    let total = 0;

    cart.forEach((item, index) => {
        total += item.price;

        const li = document.createElement("li");
        li.className = "flex justify-between items-center bg-orange-50 p-3 rounded-xl";

        li.innerHTML = `
            <div>
                <p class="font-semibold">${item.name}</p>
                <p class="text-sm text-gray-500">€ ${item.price.toFixed(2)}</p>
            </div>
            <button onclick="removeFromCart(${index})" class="text-red-600 font-bold text-xl">✕</button>
        `;

        cartItems.appendChild(li);
    });

    cartTotal.innerText = total.toFixed(2);

    if (cartCount) {
        cartCount.innerText = cart.length;
    }
}

function removeFromCart(index) {
    cart.splice(index, 1);
    saveCart();
    updateCart();
}

function openCart() {
    document.getElementById("cart-drawer").classList.remove("translate-x-full");
}

function closeCart() {
    document.getElementById("cart-drawer").classList.add("translate-x-full");
}

function toggleMenu() {
    document.getElementById("mobile-menu").classList.toggle("hidden");
}

function checkout() {
    if (cart.length === 0) {
        alert("Your cart is empty!");
        return;
    }

    let total = cart.reduce((sum, item) => sum + item.price * (item.quantity || 1), 0);

    fetch("/checkout", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            cart: cart,
            total: total
        })
    })
    .then(response => response.json())
    .then(data => {
        cart = [];
        saveCart();
        updateCart();
        window.location.href = "/order-confirmation/" + data.order_id;
    })
    .catch(error => {
        console.error("Checkout error:", error);
        alert("Something went wrong during checkout.");
    });

}

document.addEventListener("DOMContentLoaded", updateCart);