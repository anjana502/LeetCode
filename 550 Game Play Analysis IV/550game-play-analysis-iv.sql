SELECT ROUND(COUNT(event_date) / COUNT(*), 2) AS fraction FROM (SELECT player_id, MIN(event_date) AS min_date FROM Activity
GROUP BY player_id) A1
LEFT OUTER JOIN Activity A2
ON (A1.player_id = A2.player_id AND DATEDIFF(A2.event_date, min_date) = 1);