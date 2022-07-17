SELECT * FROM world.cities;

SELECT countries.name, COUNT(cities.name) as cities FROM cities JOIN countries ON cities.country_code = countries.code GROUP BY countries.name ORDER BY COUNT(cities.name) DESC;

SELECT cities.name, cities.population, cities.country_id FROM cities JOIN country ON cities.country_code = country.Code WHERE country.Code = 'MEX' AND cities.population >= 500000 ORDER BY population DESC;