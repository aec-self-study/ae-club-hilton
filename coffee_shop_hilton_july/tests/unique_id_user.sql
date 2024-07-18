with c as (select 
  customer_id
  , count(distinct visitor_id) as check
from {{ ref('user_stitching') }}
where customer_id is not null
group by 1)

select check from c  where check > 1