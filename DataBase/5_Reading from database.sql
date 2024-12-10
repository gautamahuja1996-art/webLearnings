-- To go inside the data,
-- use students_data;

-- Fetching something from the database using where clause: filtering
/*
select id, name, age
from students_data
where (age <= 20)
*/

-- fetching all columns
select * from students_data
where age = 20