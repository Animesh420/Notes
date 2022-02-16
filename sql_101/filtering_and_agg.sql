--HAVING CLAUSE TO FIND THE SUBGROUP
select 
	cd.department_name, count(*) 
from 
	data_sci.employees e
join 
	data_sci.company_departments cd 
on 
	e.department_id = cd.id

group by cd.department_name
having count(*) > 50
order by cd.department_name 

--SUBQUERIES FOR COLUMN VALUES
select 
	e1.last_name,
	e1.salary,
	e1.department_id,
	round((select avg(e2.salary) from data_sci.employees e2 where e1.department_id = e2.department_id), 2) as avg_dep_salary
from 	
	data_sci.employees e1 order by avg_dep_salary  desc

--SUBQUERIES IN FROM CLAUSE
select round(avg(salary), 2) 
from 
	(select * from data_sci.employees where salary > 100000) as new_data

--SUBQUERIES IN WHERE CLAUSE
select 
	department_id
from 
	data_sci.employees e1
where 
	(select avg(salary) from data_sci.employees e2) > e1.salary

-- USE ROLLUP TO CREATE SUBTOTALS
select 
	cr.country_name, cr.region_name, count(e.*)
from 
	data_sci.employees e 
join 	
	data_sci.company_regions cr 
on
	e.region_id = cr.id 
group by 
 rollup(cr.country_name, cr.region_name)
 order by cr.country_name, cr.region_name

--USE CUBE TO TOTAL ACROSS DIMENSIONS
select 
	cr.country_name, 
	cr.region_name,
	cd.department_name,
	count(e.*)
from data_sci.employees e
join
	data_sci.company_regions cr 
on
	e.region_id = cr.id 
join 
	data_sci.company_departments cd
on 
	e.department_id = cd.id 
group by 
	cube(cr.country_name, 
		 cr.region_name,
		 cd.department_name)
having cr.region_name is null and cr.country_name is null
order by 
	cr.country_name, 
	cr.region_name,
	cd.department_name

-- USE TOP-N Queries
select 
	*
from 
	data_sci.employees
order by salary desc fetch first 10 rows only -- standard sql





