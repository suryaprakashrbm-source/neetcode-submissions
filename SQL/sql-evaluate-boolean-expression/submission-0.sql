-- Write your query below

with temp as (
    select expressions.left_operand as left_operand,expressions.right_operand as right_operand,expressions.operator as operator, variables.Value as left_value from expressions join variables on expressions.left_operand=variables.name
)


select temp.left_operand, temp.operator ,temp.right_operand, CASE
    when temp.operator='>' and temp.left_value>variables.value then 'true'
    when temp.operator='<' and temp.left_value<variables.value then 'true' 
    when temp.operator='=' and temp.left_value=variables.value then 'true'
    else 'false'
    END
    as value
from temp join variables on variables.name=temp.right_operand 