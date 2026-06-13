select distinct
    id as order_id,
    customer_id,
    order_date,
    year(order_date) as order_year,
    month(order_date) as order_month,
    day(order_date) as order_day,
    total_amount,
    status as order_status
from {{ source('raw_data', 'orders')}}