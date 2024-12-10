-- use students;

# SELECT count(age) as 'total_students_between_18_and_24' from students_data WHERE age BETWEEN 18 AND 24;
# SELECT sum(age) from students_data WHERE age BETWEEN 18 and 24;
# SELECT avg(age) from students_data;
# SELECT min(age) from students_data;
SELECT max(age) from students_data;