-- use students;

-- delete query
-- DELETE FROM students_data WHERE id in (2, 9);

-- let's insert new data. No need to enter id, it is made auto incremental
/*
We deleted entry with id (primary key) 2 and 9. They got deleted, but when we try to insert new data (id is auto incremental),
it got inserted as id = 10. 
*/
/*
INSERT INTO students_data (name, email, age)
VALUES ('mihir', 'mihir.chawla@sunstone.in', '44')
*/

-- let's try to insert at id = 2
-- we were able to insert at id = 2
INSERT INTO students_data (id, name, email, age)
VALUES (2, 'mayush', 'mayush.verma@sunstone.in', '28')
