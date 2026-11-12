SELECT 
    category,
    SUM(quantity * unit_price) AS total_revenue,
    SUM(quantity) AS total_quantity,
    COUNT(*) AS total_orders
FROM orders
GROUP BY category
HAVING total_revenue > 300000;