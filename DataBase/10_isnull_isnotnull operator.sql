-- Adding null entries in the table first.
-- select the database
-- use students;

-- Inserting null values
/*
INSERT INTO students_data
VALUES
('8', 'Jenny', 'jenny.ahuja@sunstone.in', null, null),
('9', 'Julie', 'julie.ahuja@sunstone.in', null, null)
*/

-- checking for null values in age column
# SELECT * FROM students_data WHERE age IS NULL;