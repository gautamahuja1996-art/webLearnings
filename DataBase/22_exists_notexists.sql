-- select * from users where exists (select id from courses where course = 'SQL');
select * from users where not exists (select id from courses where course = 'SQL');