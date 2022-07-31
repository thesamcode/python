SELECT * FROM shows_schema.shows;

INSERT INTO shows (title, network, release_date, description, user_id) VALUES ('Frontier', 'Netflix', '2019-1-1', 'A show about the fur trade during the time of the Hudson Bay Co.', 1);

UPDATE shows SET release_date = '2019-01-01' WHERE release_date = '0000-00-00';
UPDATE shows SET description = 'A show about the fur trade during the time of the Hudson Bay Co.';
UPDATE shows SET user_id = '2' WHERE user_id = '1';

SELECT * FROM shows JOIN users ON users.id = shows.user_id;

SET sql_safe_updates=0;
