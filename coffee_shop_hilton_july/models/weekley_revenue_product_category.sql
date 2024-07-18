-- Revenue on a weekly basis by product category
select
    week, 
    category,
    sum(price) as revenue
from {{ ref('coffee_orders') }} r
group by category,  week
order by week, category