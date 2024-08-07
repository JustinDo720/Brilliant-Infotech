-- Creating Datanase for class
CREATE DATABASE brilliant_infotech;

-- Using Database 
USE brilliant_infotech;

-- Creating Salesman Table 
CREATE TABLE salesman(
	salesman_id INT AUTO_INCREMENT PRIMARY KEY,
    salesman_name varchar(50),
    city varchar(50),
    commission int
);

-- Inserting some values to test 
INSERT INTO salesman(salesman_name, city, commission)
VALUES ('Justin', 'City1', 2500), ('James', 'City2', 3500), ('Jack', 'City3', 1500);

-- Inserting some values to test Rome and Paris
INSERT INTO salesman(salesman_name, city, commission)
VALUES ('Muffin', 'Paris', 2500), ('Blue', 'Rome', 3500), ('Logan', 'Paris', 1500);

-- Not Live in Rome or Paris (We use and because we want both conditions to be True
SELECT salesman_id, salesman_name, city, commission FROM salesman 
WHERE city <> 'Rome' AND city <> 'Paris';

-- Name starts with any letter within A and K 
INSERT INTO salesman(salesman_name, city, commission)
VALUES ('Allen', 'Paris', 2500), ('Kim', 'Another City', 5000);

SELECT * FROM salesman
WHERE salesman_name LIKE 'a%' or salesman_name LIKE 'k%';

-- Name start with first character 'N' and fourth character is 'l' and rest may be character
INSERT INTO salesman(salesman_name, city, commission)
VALUES ('Niiles', 'City3', 500), ('Nelly', 'City10', 45000);

SELECT * FROM salesman
WHERE salesman_name LIKE 'N__l%';

