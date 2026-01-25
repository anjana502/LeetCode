SELECT E.name, B.bonus FROM Employee E LEFT OUTER JOIN
Bonus B ON
E.empID = B.empID
WHERE (B.bonus IS NULL OR B.bonus < 1000);