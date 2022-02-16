-- Common table expressions
with 
region_salaries as  -- CTE 1
(select region_id, sum(salary)as region_salary
from data_sci.employees
group by region_id),

top_region_salaries as -- CTE 2
(select region_id from region_salaries where region_salary > (select sum(region_salary)/ 7 from region_salaries))

select 
* 
from 
	region_salaries
where 
	region_id in (select region_id from top_region_salaries)


-- Adding new data for recursive CTE
drop table if exists data_sci.org_structure;
create table data_sci.org_structure (
	id integer,
	department_name text,
	parent_department_id integer
);

insert into data_sci.org_structure values 
(1, 'CEO Office', null),
(2, 'VP Sales', 1),
(3, 'VP Operations', 1),
(4, 'Northeast sales', 2),
(5, 'Northwest sales', 2),
(6, 'Infrastructure Operations', 3),
(7, 'Management Operations', 3);

with recursive  report_structure (id, department_name, parent_department_id) as 
	(select id, department_name, parent_department_id from data_sci.org_structure where  id=1
	union
	select os.id, os.department_name, os.parent_department_id from data_sci.org_structure os 
	join report_structure rs 
	on rs.parent_department_id = os.id)
	
select * from report_structure