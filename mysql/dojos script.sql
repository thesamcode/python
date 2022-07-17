SELECT * FROM dogos_and_ninjas_schema.dojos;

INSERT INTO dojos (name) VALUES ('yellow dojo');
INSERT INTO dojos (name) VALUES ('orange dojo');
INSERT INTO dojos (name) VALUES ('purple dojo');

DELETE FROM dojos WHERE id = 1;
DELETE FROM dojos WHERE id = 2;
DELETE FROM dojos WHERE id = 3;