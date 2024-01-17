-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, AVG(temperature) AS avg_temp temperatures GROUP BY city ORDER BY avg_temp DESC;
