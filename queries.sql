USE hungry_hare;

SELECT * FROM users;
SELECT * FROM products;
SELECT * FROM orders;

UPDATE users
SET role='admin'
WHERE email='jayanthi@gmail.com';