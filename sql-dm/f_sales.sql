select fo.order_id 
	,	fo.customer_id
	,	fo.product_id
	,	fo.order_id status_id
	,	dd.date_id purchase_date
	,	fo.price
	,	fo.freight_value
	,	fo.payment_value
from f_orders fo 
left join d_date dd on dd.day = extract(day from order_purchase_date) and 
						dd.month = extract(month from order_purchase_date) and 
                        dd.year = extract(year from order_purchase_date) 
