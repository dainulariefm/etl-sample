select prd.product_id
    , prd.product_category_name
    , pct.product_category_name_english
    , prd.product_name_lenght product_name_length
    , prd.product_description_lenght product_description_length
    , prd.product_photos_qty
    , prd.product_weight_g
    , prd.product_length_cm
    , prd.product_height_cm
    , prd.product_width_cm
from products prd
left join product_category_name_translation pct on prd.product_category_name = pct.product_category_name
