-- Connects all visitor_id's to a given customer_id (if they log in)
with c as (
select 
  visitor_id
  , customer_id
  , page
  , device_type
  , timestamp
  , first_value(customer_id IGNORE NULLS) over 
    (partition by visitor_id order by case when customer_id is null then 0 else 1 end desc, timestamp desc) 
    as _group
from `analytics-engineers-club.web_tracking.pageviews`
order by visitor_id, timestamp desc
)

-- Creates a new visitor_id unique for each customer (but standard across visits) (visitor_id will still be NULL if no one logged in)
select 
  visitor_id as visitor_id_raw
  , c.customer_id
  , case when _group is null then visitor_id 
  else first_value(visitor_id) over (partition by _group order by timestamp desc) end as visitor_id
  , _group
  , device_type
  , timestamp
  , page
from c
order by timestamp