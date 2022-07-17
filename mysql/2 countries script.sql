SELECT * FROM world.countries;

SELECT countries.name, countries.surface_area, countries.population FROM world.countries WHERE surface_area < 501 AND countries.population > 100000 ORDER BY name ASC;

SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy FROM world.countries WHERE countries.government_form = 'Constitutional Monarchy' AND countries.capital > 200 AND countries.life_expectancy > 75

SELECT countries.region, COUNT(countries.name) as countries FROM world.countries GROUP BY countries.region ORDER BY COUNT(countries.name) DESC;