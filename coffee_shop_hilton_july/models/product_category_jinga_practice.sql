select
  date_trunc(created_at, month) as date_month,

{% for product_category in ['coffee beans', 'merch', 'brewing supplies'] %}

    sum(case when category = '{{product_category}}' then total end) as {{product_category | replace(" ","_")}}_amount,

{% endfor %}

from {{ ref('coffee_orders') }}
group by 1