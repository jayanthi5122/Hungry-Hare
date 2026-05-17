let cart = JSON.parse(localStorage.getItem("hungryHareCart")) || [];

function saveCart() {
    localStorage.setItem("hungryHareCart", JSON.stringify(cart));
}

function addToCart(name, price) {
    price = Number(price);

    cart.push({
        name: name,
        price: price
    });

    saveCart();
    updateCart();
    openCart();
}

function updateCart() {
    const cartItems = document.getElementById("cart-items");
    const cartTotal = document.getElementById("cart-total");
    const cartCount = document.getElementById("cart-count");
    const mobileCartCount = document.getElementById("mobile-cart-count");

    if (!cartItems || !cartTotal) {
        return;
    }

    cartItems.innerHTML = "";

    let total = 0;

    cart.forEach((item, index) => {
        total += Number(item.price);

        const li = document.createElement("li");
        li.className = "flex justify-between items-center bg-orange-50 p-3 rounded-xl";

        li.innerHTML = `
            <div>
                <p class="font-semibold">${item.name}</p>
                <p class="text-sm text-gray-500">€ ${Number(item.price).toFixed(2)}</p>
            </div>

            <button onclick="removeFromCart(${index})" class="text-red-600 font-bold text-xl">
                ✕
            </button>
        `;

        cartItems.appendChild(li);
    });

    cartTotal.innerText = total.toFixed(2);

    if (cartCount) {
        cartCount.innerText = cart.length;
    }

    if (mobileCartCount) {
        mobileCartCount.innerText = cart.length;
    }
}

function removeFromCart(index) {
    cart.splice(index, 1);
    saveCart();
    updateCart();
}

function openCart() {
    const drawer = document.getElementById("cart-drawer");

    if (drawer) {
        drawer.classList.remove("translate-x-full");
    }
}

function closeCart() {
    const drawer = document.getElementById("cart-drawer");

    if (drawer) {
        drawer.classList.add("translate-x-full");
    }
}

function toggleMenu(){

    const menu = document.getElementById("mobile-menu");

    if(menu){

        menu.classList.toggle("hidden");

    }
}

function checkout() {
    if (cart.length === 0) {
        alert("Your cart is empty!");
        return;
    }

    alert("Order placed successfully!");

    cart = [];
    saveCart();
    updateCart();
    closeCart();
}

document.addEventListener("DOMContentLoaded", updateCart);