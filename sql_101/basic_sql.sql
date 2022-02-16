-- Statistical Aggregate functions
select department_id,
sum(salary) as sal_sum, 
round(avg(salary), 2) as avg_sal, 
round(var_pop(salary), 2) as var_sal,
round(stddev_pop(salary), 2) as std_sal
from data_sci.employees
group by department_id order by sal_sum, avg_sal

-- Grouping and Filtering data
select 
last_name,
	 sum(salary)
from 
	data_sci.employees
where 
	last_name like 'b%d'
or salary > 100000
group by last_name

-- Joining and Filtering data
select 
e.last_name ,
cr.region_name, cr.country_name
-- cd.department_name as department_name
from  data_sci.employees as e
join data_sci.company_regions as cr on e.region_id = cr.id
-- join data_sci.company_departments as cd on e.department_id = cd.id
where cr.country_name = 'canada'

