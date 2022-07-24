SELECT * FROM recipes_schema.recipes;

INSERT INTO recipes (name, description, instructions, date_cooked, under_30, user_id) VALUES ('Pasta', 'Noodles with sauce', 'Mix noodles with sauce', 01/01/2020, 'yes', 1);

UPDATE drivers SET id = 8 WHERE id = 9;SELECT * FROM recipes JOIN users ON users.id = recipes.user_id;