-- Write your query below
select employee_id ,
CASE
 when  employee_id %2!=0 and name not like 'M%' Then salary
 else
 0
 END as bonus 

from employees 
Order by employee_id