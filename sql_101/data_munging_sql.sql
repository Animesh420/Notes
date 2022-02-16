-- Reformat character data
select 
	upper(department_name) ,
	initcap(department_name),
from 
	data_sci.company_departments
select 
rtrim(ltrim(' Kelly ')) = 'Kelly'

select 
job_title ||  '-' || last_name,
concat(job_title, '-', last_name) as conc,
job_title ||  '-' || NULL,
concat(job_title, '-', NULL) as conc,
concat_ws('-', job_title, last_name, email) as conc_ws
from data_sci.employees

-- EXTRACT SUBSTRING OUT OF LARGER STRING
select 
substring('random bull shit' from  1 for 3) test_string,
substring('random bull shit' ,1 , 3) test_string_2,
substring('random bull shit', 3) as ts3

select * from data_sci.employees
where job_title like '%assistant%'

select job_title, (job_title like '%assistant%') is_assistant 
from data_sci.employees

-- FILTER WITH REGULAR EXPRESSION
select distinct job_title
from data_sci.employees 
where 
job_title similar to '(vp%|web%|%engineer%)'

select distinct job_title
from data_sci.employees 
where 
job_title similar to 'vp (a|m)%'

--REFORMAT NUMERIC DATA
select 
	round(avg(salary), 2),
	ceiling(avg(salary)),
	floor(avg(salary)),
	trunc(avg(salary))
from 
	data_sci.employees

-- SOUNDEX
create extension if not exists fuzzystrmatch;
select soundex('Postgres') = soundex('Postgresss'), 'Postgres' = 'Postgresss'
select soundex('Postgres'), soundex('Kostgres'),
difference('Postgres', 'Kostgres'),
levenshtein('Postgres', 'Dostgresss')
	

