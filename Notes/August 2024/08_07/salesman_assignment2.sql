show databases;

use brilliant_infotech;

show tables;
select * from salesman;

truncate salesman2;

alter table salesman
drop column commission;

-- adding the new columns
alter table salesman;

create table salesman2(
	salesman_id int primary key auto_increment,
    customer_id int,
    ord_date date,
    purch_amt float,
    ord_no int
);

insert into salesman2(customer_id, ord_date, purch_amt, ord_no)
values (3005, '2012-10-05', 150.5, 70001 ), (3001, '2012-10-05', 150.5, 70001 ), (3005, '2012-09-10', 270.65, 70009), (3002, '2012-10-05', 65.26, 70002), (3005, '2012-10-05', 150.5, 70004);

-- highest purchase amount ordered by each customer on a particular date 
select ord_date, max(purch_amt) as 'Highest Purchase'
from salesman2
group by ord_date;

select * from salesman2;
