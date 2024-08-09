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

select * from salesman3;
select * from customer;

-- customers with grade < 300: return cust name, city grade, salesman and sal city. ascen based on cust id
select customer_id, cust_name, customer.city as "Customer City", grade,  salesman_name, salesman3.city as "Salesman City"
from customer, salesman3
where grade < 300
and customer.sal_id = salesman3.salesman_id
order by customer_id ASC;

select customer_id, cust_name, customer.city, grade,  salesman_name, salesman3.city
from customer 
full join salesman3
where grade < 300
order by customer_id ASC;

select * from customer;


