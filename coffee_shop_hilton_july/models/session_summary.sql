select 
    session_id
    , session_start_time
    , session_end_time
    , device_type
    , timestamp_diff(cast(session_end_time as timestamp), cast(session_start_time as timestamp), SECOND) as session_seconds
    , count(distinct page) as unique_pages
    , case when 
        sum(case when page = 'order-confirmation' then 1 else 0 end) > 0 then 1 
        else 0 end as ended_in_puchase
from  {{ ref('session_id_creation') }}
group by 1, 2, 3, 4
order by 2, 1