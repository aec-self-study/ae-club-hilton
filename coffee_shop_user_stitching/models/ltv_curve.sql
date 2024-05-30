
-- List of all unique customers
with customers_list as (select distinct(customer_id) from `aec-students.dbt_hilton.coffee_orders`)
-- List of all weeks in data set
, week_list as (select distinct(week) from `aec-students.dbt_hilton.coffee_orders`)
-- Weekly revenue of each customer any week they spent money
, customer_week as (
    select 
      customer_id
      , week
      , sum(total) as revenue
    from `aec-students.dbt_hilton.coffee_orders`
    group by 1,2)
-- List of all combinations of weeks and customers (one row for every customer every week)
, customer_week_list as (
    select customers_list.customer_id, week_list.week
    from customers_list 
    cross join week_list)
-- Joining above data sets together to get a data set on the weekly revenue with one row per customer per week
, ltv as (
    select 
      customer_week_list.week
      , customer_week_list.customer_id
      , case when revenue is null then 0 else revenue end as revenue
      , sum(revenue) over (partition by customer_week_list.customer_id order by customer_week_list.week) as cumulative_revenue
    from customer_week_list 
    full join customer_week
    on customer_week_list.week=customer_week.week AND customer_week_list.customer_id=customer_week.customer_id
    order by customer_id, week
)
-- Filtering above data set so it starts for each customer the week they palced their first order
select * from ltv where cumulative_revenue is not null