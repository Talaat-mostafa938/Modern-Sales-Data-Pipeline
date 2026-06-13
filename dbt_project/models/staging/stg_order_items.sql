select DISTINCT
    id as order_item_id,
    order_id,
    product_id,
    quantity,
    unit_price,
    (quantity * unit_price) as total_price
from {{ source('raw_data', 'order_items')}}