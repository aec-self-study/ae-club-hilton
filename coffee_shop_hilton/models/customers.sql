-- Creating order count and finding date of first order
with first_order as (
    select 
      customer_id,
      count(*) as number_of_orders,
      min(created_at) as first_order_at
    from `analytics-engineers-club.coffee_shop.orders` 
  group by customer_id
  )

-- Grabbing name/ email from customer table
select 
  first_order.customer_id,
  c.name,
  c.email,
  first_order.first_order_at,
  first_order.number_of_orders
from
  first_order

-- Joining with above info
join `analytics-engineers-club.coffee_shop.customers` c
  on first_order.customer_id=c.id

-- Ordering by first order date
order by first_order_at