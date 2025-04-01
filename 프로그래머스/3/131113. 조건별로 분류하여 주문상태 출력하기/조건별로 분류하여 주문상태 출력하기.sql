SELECT ORDER_ID, PRODUCT_ID, 
    DATE_FORMAT(OUT_DATE, '%Y-%m-%d') AS OUT_DATE, 
    CASE
        WHEN OUT_DATE IS NULL THEN '출고미정'
        WHEN OUT_DATE <= DATE('2022-05-01') THEN '출고완료'
        ELSE '출고대기'
    END AS 출고여부
FROM FOOD_ORDER
ORDER BY ORDER_ID;

# 먼저, 데이트 형식을 DATE_FORMAT으로 문제의 조건에 맞게 년도 월 일 이 출력되도록 함
# CASE문을 사용해 '출고여부' 라는 컬럼을 새로 만들고, OUT_DATE 가 출고와 관련된 자료이기 때문에 이걸 활용해서 출고 미정과 완료, 대기의 케이스를 나눔.
# 주문 ID 로 오름차순 정렬
