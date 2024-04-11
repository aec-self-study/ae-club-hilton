
select
    r.week, 
    p.category,
    sum(r.price) as revenue
from {{ ref('coffee_orders') }} r
    left join `analytics-engineers-club.coffee_shop.products` p
    on r.product_id = p.id
group by category,  week
order by week, category