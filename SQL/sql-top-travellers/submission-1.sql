-- Write your query below


select u1.name , CASE when sum(r1.distance) is null then 0 else sum(r1.distance) END as travelled_distance  from users u1 left join rides r1 on u1.id=r1.user_id  group by u1.id order by  travelled_distance desc , u1.name