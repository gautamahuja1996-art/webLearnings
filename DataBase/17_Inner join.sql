/*
This query is applying an inner join considering employees db as base, with cities db, 
which means all the data from cities db will be fetched and joined into the employees db where the
condition employees.city_id = cities.id
*/
SELECT * FROM employees
INNER JOIN cities
ON employees.city_id = cities.id;