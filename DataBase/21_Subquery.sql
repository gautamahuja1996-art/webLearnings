-- let's find the users who are doing SQL course
/*
select id from courses where course = 'SQL';
The above query returns '2'
*/
select * from users where course_id = (select id from courses where course = 'SQL');