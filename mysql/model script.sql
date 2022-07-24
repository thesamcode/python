-- SELECT * FROM july_drivers_db.drivers;
SET SQL_SAFE_UPDATES = 0;
SET SQL_SAFE_UPDATES = 1;
users
-- C R U D CREATE, READ, UPDATE, DELETE

-- C
-- structure: INSERT INTO table_name (column_name_1, column_name_2) VALUES ('value_1', 'value_2');
INSERT INTO drivers (first_name, last_name, email, phone_num, level) VALUES ('tyler', 'tbo', 'tt@email.com', 123456789, 1);
INSERT INTO drivers (first_name, last_name, email, phone_num, level) VALUES ('Bennett', 'Lanzetta', 'bl@email.com', 0987654321, 1);
INSERT INTO drivers (first_name, last_name, email, phone_num, level) VALUES ('Ryan', 'Porper', 'rp@email.com', 0987654321, 1);
INSERT INTO drivers (first_name, last_name, email, phone_num, level) VALUES ('Madhav', 'Asok', 'rp@email.com', 0987654321, 1);
INSERT INTO drivers (first_name, last_name, email, phone_num, level) VALUES ('Ryan', 'Sutherland', 'rs@email.com', 0987654321, 1);

INSERT INTO cars (make, model, year) VALUES ('ford', 'focus', 1999);
INSERT INTO cars (make, model, year) VALUES ('honda', 'cr-v', 2015);
INSERT INTO cars (make, model, year) VALUES ('dodge', 'charge', 2020);
INSERT INTO cars (make, model, year) VALUES ('toyota', 'tundra', 2016);
INSERT INTO cars (make, model, year) VALUES ('subaru', 'legacy', 1932);



-- R
-- structure: SELECT columns FROM table_name // SELECT columns FROM table_name WHERE condition = something
SELECT * FROM drivers;
SELECT * FROM drivers WHERE first_name = 'Ryan';
SELECT * FROM drivers WHERE id = 4;

-- primary table | secondary table
SELECT * FROM drivers
-- JOIN addresses ON drivers.id = addresses.driver_id;
LEFT JOIN addresses ON drivers.id = addresses.driver_id;

-- U
-- structure: UPDATE table_name SET column_name = value, column2_name = value2 WHERE id=#;
UPDATE drivers SET last_name = 'Lanzetta', first_name="Bennett" WHERE id = 2;
UPDATE drivers SET id = 8 WHERE id = 9;

-- D
-- structure: DELETE FROM table_name WHERE id=#;
DELETE FROM drivers WHERE id = 3;
DELETE FROM drivers WHERE id in (4,6); 

SET sql_safe_updates=0;