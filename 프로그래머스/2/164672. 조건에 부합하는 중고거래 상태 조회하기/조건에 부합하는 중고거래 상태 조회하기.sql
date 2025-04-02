SELECT BOARD_ID, WRITER_ID, TITLE, PRICE, 
    CASE 
        WHEN STATUS = 'SALE' THEN '판매중'
        WHEN STATUS = 'RESERVED' THEN '예약중'
        WHEN STATUS = 'DONE' THEN '거래완료'
    END AS STATUS
FROM USED_GOODS_BOARD
WHERE CREATED_DATE = '2022-10-05'
ORDER BY BOARD_ID DESC;

# CASE 문을 통해 STATUS 가 SALE, RESERVED, DONE 에 맞게 각각에 대응하는 문자열이 나오도록 함. 
# WHERE 절을 통해 2022년 10월 5일 값이 나오도록 함. 
# DESC 에서 게시글 ID에 대해 내림차순으로 진행 
