-- creating a new database
-- CREATE DATABASE test;

-- using that db
-- use test;

-- creating 3 new tables in it
-- drop table cities;
/*
CREATE TABLE courses(
	id INT NOT NULL,
    course VARCHAR(100),
    PRIMARY KEY(id)
);
*/
/*
CREATE TABLE cities(
	id INT NOT NULL,
    city VARCHAR(100),
    PRIMARY KEY(id)
);
*/
/*
CREATE TABLE users(
	id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    course_id INT,
    city_id INT,
    PRIMARY KEY(id),
    FOREIGN KEY(course_id) REFERENCES courses(id),
    FOREIGN KEY(city_id) REFERENCES cities(id)
);
*/

-- inserting elements in all the dbs to perform the join
/*
INSERT INTO cities
VALUES 
(1, 'Delhi'),
(2, 'Agra'),
(3, 'Lucknow'),
(4, 'Bangalore'),
(5, 'Mumbai'),
(6, 'Rajasthan'),
(7, 'Sikkim'),
(8, 'Kashmir');
*/

/*
INSERT INTO courses
VALUES
(1, 'Full stack development'),
(2, 'SQL'),
(3, 'Application development'),
(4, null),
(5, 'Machine Learning');
*/

/*
INSERT INTO users
VALUES
(1, 'Gautam', 'gautam@gmail.com', 1, 3),
(2, 'Gouri', 'gouri@gmail.com', 2, 8),
(3, 'Rishabh', 'rishabh@gmail.com', 5, 6),
(4, 'Jayant', 'jayant@gmail.com', 2, 2),
(5, 'Chirag', 'chirag@gmail.com', null, 1),
(6, 'Anirudh', 'anirudh@gmail.com', 4, null)
*/

-- committing the changes
-- COMMIT;

-- multiple join query

select * from users 
inner join cities
on users.city_id = cities.id
inner join courses
on users.course_id = courses.id;
