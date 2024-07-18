select
  customer_id,
  count(*) as number_of_orders
 
from {{ ref('customers') }}
where customer_id is not null
group by customer_id
having count(*) > 1