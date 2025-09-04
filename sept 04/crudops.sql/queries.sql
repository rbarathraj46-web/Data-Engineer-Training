CREATE DATABASE hexadb;
USE hexadb;

CREATE TABLE departments (
  dept_id INT PRIMARY KEY AUTO_INCREMENT,
  dept_name VARCHAR (50) NOT NULL,
  location VARCHAR (50)
);

INSERT INTO departments (dept_id, dept_name, location) VALUES
  (1, 'IT', 'Banglore'),
  (2, 'HR', 'Hyderabad'),
  (3, 'Finance', 'Mumbai'),
  (4, 'Marketing', 'Delhi'),
  (5, 'Operations', 'Chennai');
  
CREATE TABLE employees (
  emp_id INT PRIMARY KEY AUTO_INCREMENT,
  frst_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  age INT,
  salary DECIMAL (10,2),
  FORIEGN KEY dept_id REFERENCES Departments(dept_id)
  );
  
INSERT INTO employees (emp_id, first_name, last_name, age, dept_id, salary) VALUES
  (101, 'Amit', 'Verma', 28, 1, 55000.00),
  (102, 'Sneha', 'Reddy', 32, 2, 60000.00),
  (103, 'Ravi', 'Sharma', 26, NULL, 48000.00),
  (104, 'Pooja', 'Iyer', 29, 4, 52000.00),
  (105, 'Arjun', 'Mehta', 35, 1, 75000.00);

SELECT e.emp_id, e.first_name, e.last_name, d.dept_name, d.location
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id
  
