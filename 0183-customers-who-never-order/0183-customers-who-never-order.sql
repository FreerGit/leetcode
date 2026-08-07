-- Write your PostgreSQL query statement below
SELECT C.name AS Customers
FROM Customers AS C
LEFT JOIN Orders ON Orders.customerId = C.id
WHERE Orders.customerId IS NULL;