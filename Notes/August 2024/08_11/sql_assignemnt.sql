show databases;
use brilliant_infotech;

-- Creating Departments Parent Database 
CREATE TABLE departments(
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    department_name VARCHAR(50)
);

-- Creating the Employees Child Database 
CREATE TABLE employee_dept(
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    salary FLOAT,
    department_id INT,
    FOREIGN KEY(department_id) 
    REFERENCES departments(department_id)
);


-- Inserting Table data 

INSERT INTO departments(department_name)
VALUES  ('Sales'), ('Engineering'), ('Human Resources');

INSERT INTO employee_dept(first_name, last_name, department_id, salary)
VALUES  ('John', 'Doe', 1, 60000.00),
        ('Jane', 'Smith', 1, 75000.00),
        ('Emily', 'Jones', 2, 95000.00),
        ('Michael', 'Brown', 2, 105000.00),
        ('Sarah', 'Davis', 3, 50000.00),
        ('David', 'Wilson', 3, 65000.00);

-- Note we use employee_id and salary in the WHERE clause without the SELECT 
SELECT first_name, last_name
FROM employee_dept
-- Tuple comparison
WHERE (employee_id, salary) IN (
    SELECT employee_id, salary
    FROM departments 
    LEFT JOIN employee_dept
    ON departments.department_id = employee_dept.department_id 
    WHERE salary > 70000.00
);

SELECT department_name, count(first_name) as 'Number of Employees'
FROM departments
LEFT JOIN employee_dept 
ON departments.department_id = employee_dept.department_id 
WHERE employee_id IN (
    SELECT employee_id
    FROM employee_dept
    -- Tuple comparison
    WHERE (employee_id, salary) IN (
        SELECT employee_id, salary
        FROM departments 
        LEFT JOIN employee_dept
        ON departments.department_id = employee_dept.department_id 
        WHERE salary > 70000.00
    )
)
GROUP BY department_name
HAVING count(first_name) >= 2;