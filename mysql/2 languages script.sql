SELECT * FROM world.languages;


SELECT countries.name, languages.language, languages.percentage FROM languages JOIN countries ON languages.country_code = countries.code WHERE languages.percentage > 89 ORDER BY percentage DESC;