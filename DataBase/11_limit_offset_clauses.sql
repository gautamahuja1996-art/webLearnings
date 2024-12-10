-- use students;

/*
This first fetches all the rows where age is between 18 and 27, including 18 and 27.
Next it fetches the top 3 rows
Finally it starts the index from 3
*/
SELECT * FROM students_data WHERE age BETWEEN 18 AND 27 LIMIT 3 OFFSET 3;