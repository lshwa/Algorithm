SELECT FLAVOR
FROM (
    SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL
    FROM (
        SELECT FLAVOR, TOTAL_ORDER FROM FIRST_HALF
        UNION ALL
        SELECT FLAVOR, TOTAL_ORDER FROM JULY
    ) AS ALL_ORDERS
    GROUP BY FLAVOR
) AS TOTAL_SUM
ORDER BY TOTAL DESC
LIMIT 3;