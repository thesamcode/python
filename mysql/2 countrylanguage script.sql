SELECT * FROM world.countrylanguage;

SELECT Name, Language, Percentage FROM countrylanguage JOIN country ON countrylanguage.CountryCode = country.code WHERE Language = 'slovene' ORDER BY Percentage DESC;