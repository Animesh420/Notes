-- INTRO TO WINDOW FUNCS
select
department_id, 
last_name,
salary,
first_value(salary) over (partition by department_id order by salary)
from data_sci.employees

-- NTH_VALUE and NTILE
select 
	department_id,
	last_name,
	salary,
	round(avg(salary) over (partition by department_id), 2)
from data_sci.employees

-- NTILE: Divides a group in N Tiles and shows the output
select 
	department_id,
	salary,
	ntile(4) over (partition by department_id order by salary desc) as quartile
from data_sci.employees

-- NTH VALUE : Gives the nth value in a group
select 
	department_id,
	salary,
	nth_value(salary, 5) over (partition by department_id order by salary desc)
from 
	data_sci.employees

-- RANK: 
select 
	department_id,
	last_name,
	salary,
	rank() over (partition by  department_id order by salary desc)
from data_sci.employees

-- LEAD AND LAG 
select 
	department_id, 
	last_name, 
	salary, 
	lead(salary, 2) over (partition by  department_id order by salary desc),
	lag(last_name, 2) over (partition by  department_id order by salary desc)
from data_sci.employees

-- WIDTH BUCKET and CUME_DIST
select 
	department_id,
	last_name,
	salary, 
	width_bucket(salary, 0, 150000, 10) as wb,
	round((cume_dist() over (order by salary desc) * 100)::numeric , 2) -- because round accepts numeric, not double
from data_sci.employees
order by wb desc


	

