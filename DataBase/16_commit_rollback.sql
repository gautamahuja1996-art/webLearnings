-- use students;
SET autocommit = 0;
UPDATE students_data SET age = 25 WHERE id = 2;
SELECT * FROM students.students_data;
COMMIT;
ROLLBACK;

UPDATE students_data SET age = 28 WHERE id = 1;
ROLLBACK;