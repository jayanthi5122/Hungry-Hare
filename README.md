# Hungry Hare 🍔

## Overview

Hungry Hare is a full-stack food ordering web application inspired by modern food delivery platforms such as Uber Eats and Deliveroo. The project was developed to demonstrate practical knowledge of frontend development, backend API development, database management, and full-stack application architecture.

The application allows users to register, log in, browse food categories, search for menu items, add products to a shopping cart, select a payment method, place orders, and view their order history.

The project was built as a graduate-level portfolio project to showcase skills commonly required for Junior Software Developer and Full-Stack Developer roles.

---

## Objectives

The primary goals of this project are:

* Develop a modern responsive web application using React.
* Build RESTful APIs using Flask.
* Store and manage application data using MySQL.
* Implement user authentication and authorization.
* Demonstrate CRUD operations.
* Understand frontend-backend communication.
* Apply software development best practices.
* Prepare for graduate software engineering interviews.

---

## Features

### User Management

* User Registration
* User Login
* Session Management
* User-specific Order History

### Food Ordering

* Browse Food Categories
* Search Food Items
* View Menu Details
* Add Items to Cart
* Update Item Quantities
* Remove Items from Cart

### Checkout and Payment

* Cash on Delivery (COD)
* Credit / Debit Card (Demo)
* Digital Wallet (Demo)
* Order Confirmation

### Order Management

* Place Orders
* Store Orders in MySQL
* View Previous Orders
* Track Order Status

### User Experience

* Responsive Design
* Modern UI inspired by food delivery applications
* Search functionality
* Category-based navigation
* Clean and intuitive interface

---

## Technology Stack

### Frontend

* React.js
* React Router
* JavaScript (ES6+)
* HTML5
* CSS3
* Tailwind CSS

### Backend

* Python
* Flask
* Flask-CORS

### Database

* MySQL

### Development Tools

* Git
* GitHub
* VS Code
* MySQL Workbench

---

## System Architecture

```text
React Frontend
       │
       ▼
 Flask REST API
       │
       ▼
   MySQL Database
```

### Data Flow

1. User interacts with the React interface.
2. React sends API requests to Flask.
3. Flask processes business logic.
4. MySQL stores and retrieves data.
5. Flask returns JSON responses.
6. React updates the user interface.

---

## Database Design

The application uses MySQL with the following tables:

### Users

Stores user account information.

```text
id
name
email
password
role
```

### Products

Stores menu categories and food items.

```text
id
name
category
price
image
```

### Orders

Stores order information.

```text
id
user_id
customer_name
total
status
created_at
```

### Order Items

Stores products associated with an order.

```text
id
order_id
item_name
price
quantity
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/hungry-hare.git
cd hungry-hare
```

---

### Backend Setup

```bash
cd backend

pip install flask
pip install flask-cors
pip install mysql-connector-python
pip install werkzeug

python3 app.py
```

Backend runs on:

```text
http://127.0.0.1:5001
```

---

### Frontend Setup

```bash
cd frontend

npm install

npm run dev -- --host 127.0.0.1
```

Frontend runs on:

```text
http://127.0.0.1:5173
```

---

### Database Setup

Create database:

```sql
CREATE DATABASE hungry_hare;
```

Import your SQL schema:

```sql
USE hungry_hare;
```

Create required tables:

* users
* products
* orders
* order_items

---

## API Endpoints

### Authentication

```http
POST /api/register
POST /api/login
```

### Products

```http
GET /api/products
GET /api/category/<category>
```

### Orders

```http
POST /api/checkout
GET /api/orders
```

---

## Learning Outcomes

Through this project, the following skills were developed:

* React Component Development
* State Management
* Routing with React Router
* REST API Design
* Flask Backend Development
* Database Design
* SQL Query Writing
* MySQL Integration
* Authentication Concepts
* Debugging and Testing
* Git Version Control

---

## Future Improvements

The following enhancements can be implemented in future versions:

* Docker Containerization
* Email Verification
* Password Reset via Email
* Google Maps Integration
* Real Payment Gateway Integration (Stripe/PayPal)
* Admin Dashboard
* Order Tracking
* Restaurant Analytics
* Cloud Deployment (AWS/Azure/GCP)

---

## Conclusion

Hungry Hare demonstrates the implementation of a complete full-stack web application using React, Flask, and MySQL. The project highlights frontend development, backend API design, database management, and software engineering principles commonly used in modern web application development.

This project serves as a practical portfolio piece for graduate software developer positions and demonstrates readiness to work with modern web technologies in a professional environment.
