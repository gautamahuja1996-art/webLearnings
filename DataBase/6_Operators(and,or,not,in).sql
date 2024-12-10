-- Going into the students db as
-- use students

-- and operator
/*
select * from students_data
where age >= 21 and age <= 27
*/

-- or operator
/*
select * from students_data
where age = 21 or age = 27 or age = 28
*/

-- not operator
/*
select * from students_data
where not age = 21 and not age = 28
*/

-- in operator

select * from students_data
where age in (21, 27, 28)





