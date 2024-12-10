/*
SELECT * FROM employees
LEFT JOIN cities
ON employees.city_id = cities.id;
*/

SELECT * FROM employees
RIGHT JOIN cities
ON employees.city_id = cities.id;