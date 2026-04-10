-- Top Selling Products
SELECT p.name, SUM(oi.quantity) AS total_sold
FROM Order_Items oi
JOIN Products p ON oi.product_id = p.product_id
GROUP BY p.name
ORDER BY total_sold DESC;

-- Most Valuable Customers
SELECT c.name, SUM(oi.quantity * p.price) AS total_spent
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Order_Items oi ON o.order_id = oi.order_id
JOIN Products p ON oi.product_id = p.product_id
GROUP BY c.name
ORDER BY total_spent DESC;

-- Monthly Revenue
SELECT TO_CHAR(o.order_date, 'YYYY-MM') AS month,
       SUM(oi.quantity * p.price) AS revenue
FROM Orders o
JOIN Order_Items oi ON o.order_id = oi.order_id
JOIN Products p ON oi.product_id = p.product_id
GROUP BY TO_CHAR(o.order_date, 'YYYY-MM')
ORDER BY month;

-- Category-wise Sales
SELECT p.category, SUM(oi.quantity * p.price) AS total_sales
FROM Order_Items oi
JOIN Products p ON oi.product_id = p.product_id
GROUP BY p.category;

-- Inactive Customers
SELECT c.name
FROM Customers c
WHERE c.customer_id NOT IN (
    SELECT DISTINCT customer_id FROM Orders
);
