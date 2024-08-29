show databases;

use bus_reservation;

CREATE table bus_res_login(
	id int primary key auto_increment,
	username varchar(100),
    password varchar(100)
);

INSERT INTO bus_res_login(username, password)
VALUES('justindo720', 'password_testing');

SELECT id, username, password
FROM bus_res_login;

CREATE TABLE bus_res_schedule(
	res_id int primary key auto_increment,
    timing datetime,
    fare float
);

INSERT INTO bus_res_schedule (timing, fare) VALUES
('2024-09-01 08:00:00', 25.50),
('2024-09-02 09:30:00', 15.75),
('2024-09-03 14:15:00', 35.00),
('2024-09-04 17:45:00', 22.25),
('2024-09-05 11:30:00', 40.00),
('2024-09-06 13:00:00', 18.50),
('2024-09-07 16:20:00', 29.75),
('2024-09-08 10:10:00', 30.00),
('2024-09-09 12:45:00', 25.00),
('2024-09-10 15:30:00', 20.00);

SELECT * FROM bus_res_schedule;

/* Creating a relationship Tab */
CREATE TABLE bus_res(
	id int primary key auto_increment, 
    username varchar(100), 
    username_id int,
    bus_id int,
    FOREIGN KEY(username_id)
		REFERENCES bus_res_login(id),
    FOREIGN KEY(bus_id)
		REFERENCES bus_res_schedule(res_id)
);

INSERT INTO bus_res(username, username_id, bus_id)
VALUES('justindo720', 1 , 4);

SELECT username, bus_id, timing, fare
FROM bus_res
LEFT JOIN bus_res_schedule 
ON bus_res.bus_id = bus_res_schedule.res_id
WHERE username_id = 1
AND username = 'justindo720'
ORDER BY reservation_time;

ALTER TABLE bus_res
ADD COLUMN reservation_time DATETIME DEFAULT CURRENT_TIMESTAMP;

DESCRIBE bus_res;
TRUNCATE TABLE bus_res;
DELETE FROM bus_res_login
WHERE id = 5;