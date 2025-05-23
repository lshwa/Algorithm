SELECT b.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY, 
    SUM(s.SALES* b.PRICE) AS TOTAL_SALES
FROM BOOK b
JOIN AUTHOR a
    ON b.AUTHOR_ID = a.AUTHOR_ID
JOIN BOOK_SALES s
    ON b.BOOK_ID = s.BOOK_ID
WHERE s.SALES_DATE BETWEEN '2022-01-01' AND '2022-01-31'
GROUP BY b.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY
ORDER BY b.AUTHOR_ID ASC, b.CATEGORY DESC;