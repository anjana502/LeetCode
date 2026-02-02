SELECT P.product_name, SUM(O.unit) AS unit FROM Products P
INNER JOIN Orders O ON
P.product_id = O.product_id
WHERE YEAR(order_date) = 2020 AND MONTH(order_date) = 02
GROUP BY O.product_id
HAVING SUM(O.unit) >= 100;