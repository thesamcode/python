SELECT * FROM shows_schema.users;

INSERT INTO users (first_name, last_name, email, password) VALUES ('John', 'Smith', 'john@email.com', '1234');

UPDATE users SET password = '1234';

DELETE FROM users WHERE id = 1;