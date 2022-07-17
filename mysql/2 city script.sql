SELECT * FROM world.city;

SELECT country.name as country_name, city.Name as city_name, city.District, city.Population FROM city JOIN country ON city.CountryCode = country.Code WHERE country.Name = 'Argentina' AND city.District = 'Buenos Aires' AND city.Population >500000 ORDER BY Population DESC;