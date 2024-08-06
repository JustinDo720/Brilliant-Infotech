-- Creatinng the Database
CREATE DATABASE coffee;

-- Using the Database
USE coffee;

-- Creating a table
CREATE TABLE coffee_order(
    id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    price float(4,2),
    coffee_type VARCHAR(30)
);

-- Alter to auto-increment our id 
ALTER table coffee_order
modify id int AUTO_INCREMENT;

-- Alter to add a column
ALTER table coffee_order
ADD order_date DATE;

-- Alter for NOT NULL constraint
ALTER TABLE coffee_order
MODIFY customer_name VARCHAR(50) NOT NULL,
MODIFY coffee_type VARCHAR(30) NOT NULL;

-- Alter for DEFAULT constraint 
ALTER TABLE coffee_order
MODIFY price int DEFAULT 0,
MODIFY order_date DATE DEFAULT (current_date());

-- Alter with a UNIQUE constraint 
ALTER TABLE coffee_order
MODIFY id INT UNIQUE,
ADD ticket_number int UNIQUE;

-- Alter with Check Constraint
ALTER TABLE coffee_order
-- Remember that the date should be in: YYYY-MM-DD
ADD CONSTRAINT date_check CHECK (order_date > '2024-08-03');


-- Initial Inserting Data
INSERT INTO coffee_order(id, customer_name, price, coffee_type, ticket_number)
VALUES(1,'Justin',1.51,'espresso', 243);

-- But since our id auto-increment
INSERT INTO coffee_order(customer_name, price, coffee_type, ticket_number)
VALUES('Thy',1.53,'Iced Coffee', 244);

-- But since our id auto-increment
INSERT INTO coffee_order(customer_name, price, coffee_type, ticket_number)
VALUES('Muffin',3.53,'americano', 245);

-- Viewing Data
SELECT * FROM coffee_order;
SELECT ticket_number, customer_name, price  FROM coffee_order;

-- Checking More Details
DESCRIBE coffee_order;
