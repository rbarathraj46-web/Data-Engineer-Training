CREATE DATABASE retail_db;
USE retail_db;
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    supplier VARCHAR(100)
);
CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    sale_date DATE,
    quantity_sold INT,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    stock_level INT,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
INSERT INTO products (product_name, category, price, supplier)
VALUES ('Laptop', 'Electronics', 55000, 'TechWorld'),
       ('Smartphone', 'Electronics', 25000, 'MobileHub'),
       ('Shampoo', 'Personal Care', 350, 'GlowCorp');

INSERT INTO sales (product_id, sale_date, quantity_sold, total_amount)
VALUES (1, '2025-10-01', 5, 275000),
       (2, '2025-10-02', 10, 250000),
       (3, '2025-10-03', 30, 10500);

INSERT INTO inventory (product_id, stock_level)
VALUES (1, 12), (2, 4), (3, 60);

SELECT * FROM products;
UPDATE inventory SET stock_level = 5 WHERE product_id = 2;
DELETE FROM sales WHERE sale_id = 3;
DELIMITER //
CREATE PROCEDURE GetLowStockItems(IN threshold INT)
BEGIN
    SELECT p.product_name, i.stock_level
    FROM products p
    JOIN inventory i ON p.product_id = i.product_id
    WHERE i.stock_level < threshold;
END //
DELIMITER ;

CALL GetLowStockItems(10);