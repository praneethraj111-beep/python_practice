SELECT * FROM inventory;-- ==========================================================
-- INVENTORY BUSINESS INTELLIGENCE REPORTING
-- ==========================================================

-- Query 1: Total Financial Valuation of Current Stock
-- Calculates total cash tied up in inventory per product
SELECT 
    product_name,
    quantity,
    price,
    (quantity * price) AS total_valuation
FROM inventory
ORDER BY total_valuation DESC;

---

-- Query 2: Low Stock Operations Alert
-- Dynamically flags items that have fallen below safety limits (e.g., fewer than 20 items)
SELECT 
    product_name,
    quantity
FROM inventory
WHERE quantity < 20;

---

-- Query 3: High-Level Inventory Metrics
-- Provides executives with total distinct products, total stock, and average product price
SELECT 
    COUNT(DISTINCT product_name) AS unique_products_count,
    SUM(quantity) AS total_units_in_warehouse,
    ROUND(AVG(price), 2) AS average_product_price
FROM inventory;