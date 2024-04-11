-- All coffee orders with price information and flags if it is a new customer
select
    item.product_id,
    item.order_id,
    coffee_orders.id,
    coffee_orders.customer_id,
    coffee_orders.created_at,
    coffee_orders.total,
    prices.price,
    case when coffee_orders.created_at = min(coffee_orders.created_at) over
     (partition by coffee_orders.customer_id) then 1 else 0 end as new_customer_flag,
    date_trunc(coffee_orders.created_at, WEEK) AS week,
from `analytics-engineers-club.coffee_shop.order_items` item
left join `analytics-engineers-club.coffee_shop.orders` coffee_orders
    on item.order_id = coffee_orders.id

left join `analytics-engineers-club.coffee_shop.product_prices` as prices
    on item.product_id = prices.product_id
    and coffee_orders.created_at between prices.created_at and prices.ended_at

order by customer_id, created_at, order_id, product_id