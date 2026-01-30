SELECT E1.employee_id, E1.name, E2.reports_count, E2.average_age FROM Employees E1
INNER JOIN (SELECT reports_to, COUNT(*) AS reports_count, ROUND(AVG(age)) AS average_age FROM Employees
GROUP BY reports_to
HAVING COUNT(*) >= 1) AS E2
ON E1.employee_id = E2.reports_to
ORDER BY E1.employee_id;