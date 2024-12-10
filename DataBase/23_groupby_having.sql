-- creating a new table
/*
create table people(
	id int not null unique,
    name varchar(100),
    email varchar(100),
    city_id int,
    primary key(id),
    foreign key(city_id) references cities(id)
)
*/

/*
 -- inserting data
 insert into people
 values 
 (1, 'gautam', 'gautam@gmail.com', 1),
 (2, 'gouri', 'gouri@gmail.com', 1),
 (3, 'rishabh', 'rishabh@gmail.com', 1),
 (4, 'chirag', 'chirag@gmail.com', 3),
 (5, 'garima', 'garima@gmail.com', 4),
 (6, 'jayant', 'jayant@gmail.com', 4),
 (7, 'cherry', 'cherry@gmail.com', 3),
 (8, 'anirudh', 'anirudh@gmail.com', 2),
 (9, 'rajan', 'rajan@gmail.com', 2),
 (10, 'jenny', 'jenny@gmail.com', 7)
 */
 
 -- committing
 -- commit;
 
 select id, city_id from people group by city_id;