-- Write your PostgreSQL query statement below
SELECT name, SUM(T.amount) AS balance
FROM Users as U
JOIN Transactions as T ON U.account = T.account 
GROUP BY U.account, U.name
HAVING SUM(t.amount) > 10000