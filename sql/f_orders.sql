select 
        oit.order_id
        , oit.order_item_id 
        , cst.customer_unique_id customer_id
        , oit.product_id
        , pct.product_category_name_english product_category
        , oit.price
        , oit.freight_value
        , ord.order_status
        , ord.order_purchase_date 
        , ord.order_approved_date 
        , ord.order_estimated_delivery_date
        , ord.order_delivered_carrier_date 
        , ord.order_delivered_customer_date 
        , oit.shipping_limit_date
        , oit.seller_id
        , op.payment_sequential 
        , op.payment_type 
        , op.payment_installments
        , op.payment_value
        , cst.customer_city
        , cst.customer_state
        , cst.customer_zip_code_prefix
        , slr.seller_city
        , slr.seller_state
        , slr.seller_zip_code_prefix
        , orv.review_score
        , orv.review_comment_title
        , orv.review_comment_message
        , orv.review_creation_date
        , orv.review_answer_date
    from order_items oit
    left join orders ord on oit.order_id = ord.order_id
    left join order_payments op on oit.order_id = op.order_id 
    left join order_reviews orv on oit.order_id = orv.order_id 
    left join customers cst on ord.customer_id = cst.customer_id
    left join products prd on oit.product_id = prd.product_id
    left join product_category_name_translation pct on prd.product_category_name = pct.product_category_name
    left join sellers slr on oit.seller_id = slr.seller_id
    order by ord.order_purchase_date desc
    
    ;