-- writing a test that will fail!
select
  customer_id,
  number_of_orders
from {{ ref('customers') }}
where number_of_orders > 1