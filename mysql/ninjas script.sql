SELECT * FROM dogos_and_ninjas_schema.ninjas;

INSERT INTO ninjas (first_name, last_name, age, dojo_id, dojo_name) VALUES ('Alfonso', 'Turo', 25, 4, 'yellow dojo');
INSERT INTO ninjas (first_name, last_name, age, dojo_id, dojo_name) VALUES ('Alan', 'Johnson', 26, 4, 'yellow dojo');
INSERT INTO ninjas (first_name, last_name, age, dojo_id, dojo_name) VALUES ('Adrian', 'Gora', 27, 4, 'yellow dojo');

INSERT INTO ninjas (first_name, last_name, age, dojo_id, dojo_name) VALUES ('Olga', 'Fanzo', 24, 5, 'orange dojo');
INSERT INTO ninjas (first_name, last_name, age, dojo_id, dojo_name) VALUES ('Omar', 'Ruiz', 23, 5, 'orange dojo');
INSERT INTO ninjas (first_name, last_name, age, dojo_id, dojo_name) VALUES ('Ophelia', 'Andel', 24, 5, 'orange dojo');

INSERT INTO ninjas (first_name, last_name, age, dojo_id, dojo_name) VALUES ('Paul', 'James', 26, 6, 'purple dojo');
INSERT INTO ninjas (first_name, last_name, age, dojo_id, dojo_name) VALUES ('Pano', 'Tron', 27, 6, 'purple dojo');
INSERT INTO ninjas (first_name, last_name, age, dojo_id, dojo_name) VALUES ('Peggy', 'Sue', 28, 6, 'purple dojo');

SELECT * FROM ninjas WHERE dojo_name = 'purple dojo';
SELECT * FROM ninjas WHERE id = 9;


