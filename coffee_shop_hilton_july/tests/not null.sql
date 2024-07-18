select *
from {{ ref('customers') }}
where customer_id is null