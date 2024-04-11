-- Revenue on a weekly basis by customer type
select
    week, 
    case when new_customer_flag = 1 then 'New Customers' else 'Returning Customers' end as customer_type,
    sum(price) as revenue
from {{ ref('coffee_orders') }}

group by customer_type, week
order by week, customer_type
