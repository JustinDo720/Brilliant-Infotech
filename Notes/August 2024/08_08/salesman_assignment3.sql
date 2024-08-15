use brilliant_infotech;

create table salesman3(
	salesman_id int auto_increment primary key,
    salesman_name varchar(50),
    city varchar(50),
    commission float
);

create table customer(
	customer_id int auto_increment primary key,
    cust_name varchar(50),
    city varchar(50),
    grade int, 
    sal_id int,
    foreign key(sal_id) references salesman3(salesman_id)
);

-- insert testing data 
insert into salesman3(salesman_name, city, commission)
values('James Hoog', 'New York', 0.15), ('Nail Knite', 'Paris', 0.13);

insert into customer(cust_name, city, grade, sal_id)
values('Nick Rimando', 'New York', 100, 1), ('Brad Davis', 'New York', 200, 1), ('Graham Zusi', 'Cali', 200, 2);

INSERT INTO customer(cust_name, city, grade, sal_id)
VALUES ('Thy', 'New York', 100, 2), ('Justin', 'New Jeresey', 100, 2);

select * from salesman3;
select * from customer;

-- customers with grade < 300: return cust name, city grade, salesman and sal city. ascen based on cust id
select customer_id, cust_name, customer.city as "Customer City", grade,  salesman_name, salesman3.city as "Salesman City"
from customer, salesman3
where grade < 300
and customer.sal_id = salesman3.salesman_id
order by customer_id ASC;

select customer_id, cust_name, customer.city, grade,  salesman_name, salesman3.city
from salesman3
right join customer
on salesman3.salesman_id = customer.sal_id
where grade < 300
order by customer_id ASC;

select * from customer;

select * from salesman3;

-- Salesman doesn't live with customer comission is Higher than 0.12
SELECT salesman_name, salesman3.city AS "Salesman City", commission, cust_name, customer.city AS "Customer City"
FROM salesman3
LEFT JOIN customer
ON salesman3.salesman_id = customer.sal_id
WHERE salesman3.city <> customer.city
AND commission > 0.12;

SELECT salesman_name, count(*) as "Number of Customers"
FROM salesman3
LEFT JOIN customer
ON salesman3.salesman_id = customer.sal_id
WHERE salesman3.city <> customer.city
AND commission > 0.12
GROUP BY salesman_name;