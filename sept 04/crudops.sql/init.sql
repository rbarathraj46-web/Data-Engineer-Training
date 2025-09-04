CREATE TABLE Orders (
  orderId INTEGER PRIMARY KEY AUTO_INCREMENT,
  customer_name VARCHAR (100) NOT NULL,
  product VARCHAR (100),
  quantity INT,
  price DECIMAL (10,2),
  order_date DATE
);

-- insert
INSERT INTO Orders (customer_name, product, quantity, price, order_date) VALUES
  ('Rahul Sharma', 'Laptop', 1, 55000.00, '2025-01-05'),
  ('Priya Singh', 'Headphones', 2, 3000.00, '2025-01-06'),
  ('Aman Kumar', 'Mobile Phone', 1, 25000.00, '2025-01-06'),
  ('Sneha Reddy', 'Keyboard', 3, 1500.00, '2025-01-07'),
  ('Arjun Mehta', 'Monitor', 2, 12000.00, '2025-01-07'),
  ('Pooja Iyer', 'Laptop', 1, 60000.00, '2025-01-08'),
  ('Ravi Sharma', 'Mouse', 5, 800.00, '2025-01-08'),
  ('Neha Kapoor', 'Tablet', 1, 20000.00, '2025-01-09'),
  ('Vikram Rao', 'Printer', 1, 8500.00, '2025-01-09'),
  ('Divya Nair', 'Laptop', 2, 58000.00, '2025-01-10');


-- fetch 
SELECT * FROM Orders WHERE order_date = '2025-01-07' ;
SELECT * FROM Orders WHERE price > 2000;
SELECT * FROM Orders WHERE product = 'Laptop';
SELECT * FROM Orders WHERE quantity > 2;
SELECT * FROM Orders ORDER BY price DESC;
SELECT * FROM Orders ORDER BY order_date, customer_name;
SELECT COUNT(*) AS total_orders FROM Orders;

SELECT AVG(price) AS average_price FROM Orders;
SELECT MAX(price) AS max_price FROM Orders;
SELECT SUM(quantity) AS total_quantity_sold FROM Orders;

SELECT product SUM(quantity * price) AS total_sales FROM Orders GROUP BY product;
SELECT product COUNT(*) AS order_count FROM Orders GROUP BY product;
SELECT customer_name AVG(price) AS average_price FROM Orders GROUP BY customer_name;

SELECT product SUM(quantity) AS total_quantity FROM orders GROUP BY product HAVING SUM(quantity) > 3;
SELECT customer_name COUNT(*) AS order_count FROM Orders GROUP BY customer_name HAVING COUNT(*) > 1;
