WITH RENT AS (
  SELECT 
    h.history_id,
    h.car_id,
    DATEDIFF(h.end_date, h.start_date) + 1 AS days
  FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY h
)
SELECT
  r.history_id,
  FLOOR(c.daily_fee * r.days * (1 - IFNULL(p.discount_rate, 0) / 100)) AS FEE
FROM RENT r
JOIN CAR_RENTAL_COMPANY_CAR c
  ON c.car_id = r.car_id
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
  ON p.car_type = c.car_type
 AND (
      (r.days >= 90 AND p.duration_type = '90일 이상') OR
      (r.days >= 30 AND r.days < 90 AND p.duration_type = '30일 이상') OR
      (r.days >= 7  AND r.days < 30 AND p.duration_type = '7일 이상')
     )
WHERE c.car_type = '트럭'
ORDER BY FEE DESC, r.history_id DESC;