-- THANK YOU MODE! : https://mode.com/blog/finding-user-sessions-sql
-- Finding time of session beforehand
with last as (select *
  , lag(timestamp) over
    (partition by visitor_id order by timestamp) as last_session
from  {{ ref('user_stitching') }}
where customer_id is not null
order by visitor_id, timestamp), 

-- Flagging if it is the first session (time gap > 30 min)
session_flags as (select *
  , timestamp_diff(timestamp, last_session, MINUTE) as time_diff
  , case when  timestamp_diff(timestamp, last_session, MINUTE) >= 30 or last_session is null then 1
    else 0 end as new_session_flag
from last)

-- Creating ID by summing flags (ordering by visitor_id's and time)
select 
    sum(new_session_flag) over (order by visitor_id, timestamp) as session_id
    , *
from session_flags
