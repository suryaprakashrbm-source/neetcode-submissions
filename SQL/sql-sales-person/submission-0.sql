-- Write your query below

select name from   sales_person   where sales_id not in (

    select orders.sales_id from orders join company on company.com_id=orders.com_id where company.name='CRIMSON'

)