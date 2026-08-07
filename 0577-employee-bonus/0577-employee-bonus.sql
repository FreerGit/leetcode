-- Write your PostgreSQL query statement below
SELECT E.name, B.bonus 
from Employee as E
LEFT JOIN Bonus as B ON E.empId = B.empId
WHERE B.bonus <  1000 or B.bonus IS NULL