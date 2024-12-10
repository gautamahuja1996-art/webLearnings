-- creating a new table cities

/*
CREATE TABLE cities(
	id INT NOT NULL UNIQUE,
    city VARCHAR(100),
    PRIMARY KEY(id)
)
*/

-- inserting data into the cities table
/*
INSERT INTO cities(id, city)
VALUES 
(1, 'Agra'),
(2, 'Delhi'),
(3, 'Rohtak'),
(4, 'Kanpur'),
(5, 'Sikkim'),
(6, 'Manipur'),
(7, 'Kashmir')
*/

-- creating a new table named employees
/*
CREATE TABLE employees(
	id INT NOT NULL UNIQUE AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    city_id INT,
    PRIMARY KEY(id),
    FOREIGN KEY(city_id) REFERENCES cities(id)
)
*/

-- inserting data into the employees table
INSERT INTO employees(id, name, email, city_id)
VALUES
(1, 'Gautam', 'gautam.ahuja@sunstone.in', 1),
(2, 'Rishabh', 'rishabh.chauhan@sunstone.in', 2),
(3, 'Chirag', 'chirag.katiyar@sunstone.in', 5)