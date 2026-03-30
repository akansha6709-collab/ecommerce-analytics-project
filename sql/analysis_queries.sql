-- Total Revenue
SELECT SUM(Purchase_Amount) AS total_revenue
FROM customer_data;

-- Total Orders
SELECT COUNT(*) AS total_orders
FROM customer_data;

-- Revenue by Category
SELECT Category, SUM(Purchase_Amount) AS total_revenue
FROM customer_data
GROUP BY Category
ORDER BY total_revenue DESC;

-- Customer Segmentation (High vs Low)
SELECT 
    High_Value_Customer,
    COUNT(Customer_ID) AS total_customers,
    SUM(Purchase_Amount) AS total_revenue
FROM customer_data
GROUP BY High_Value_Customer;

-- Average Order Value (AOV)
SELECT 
    SUM(Purchase_Amount) / COUNT(*) AS avg_order_value
FROM customer_data;

-- Revenue by Age Group
SELECT 
    age_group,
    SUM(Purchase_Amount) AS total_revenue
FROM customer_data
GROUP BY age_group
ORDER BY total_revenue DESC;
