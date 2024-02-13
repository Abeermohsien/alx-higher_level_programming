-- Display the 3 cities hightest temperature.
SELECT City, AVG(Value) AS avg_temp
FROM temperatures
WHERE month = 7 or month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
