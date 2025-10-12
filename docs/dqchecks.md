# Data Quality Checks
- **Row Count**: each `dt` partition > 0
- **Required Columns**: `order_id`, `product_id`, `add_to_cart_order`
- **Nulls**: reject if `product_id` null rate > 0.1%
- **Domain**: `aisle_id`, `department_id` > 0
- **Schema Drift**: exact column set for dim tables
