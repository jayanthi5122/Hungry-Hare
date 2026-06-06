USE hungry_hare;

SELECT * FROM users;

SELECT * FROM products;

SELECT * FROM orders;

SELECT * FROM order_items;


UPDATE users
SET role='admin'
WHERE email='jayanthi@gmail.com';
SELECT id, name, email, role FROM users;