select 
    products.name
    , prices.product_id
    , products.category
    , prices.price
    , prices.created_at
    , prices.ended_at
from  `analytics-engineers-club.coffee_shop.product_prices` prices
left join `analytics-engineers-club.coffee_shop.products` as products
    on  prices.product_id = products.id