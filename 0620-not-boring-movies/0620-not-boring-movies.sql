-- Write your PostgreSQL query statement below
SELECT * FROM Cinema as C
WHERE c.id % 2 = 1 and C.description != 'boring'
ORDER BY c.rating desc