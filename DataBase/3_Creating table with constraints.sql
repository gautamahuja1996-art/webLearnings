-- creating a table in the students database.
-- First we have to use it as,
-- use students;

 -- Creating a table in it with constraints
 create table students_data(
	id int not null unique,
    name varchar(100) not null,
    email varchar(100) not null unique,
    age tinyint check (age >= 18),
    status boolean default 1
 )