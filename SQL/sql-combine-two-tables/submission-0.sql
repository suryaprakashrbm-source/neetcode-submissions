-- Write your query below
select p1.first_name,p1.last_name,a1.city,a1.state from person p1 left join address a1 on p1.person_id=a1.person_id