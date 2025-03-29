SELECT b.TITLE, b.BOARD_ID, r.REPLY_ID, r.WRITER_ID, r.CONTENTS, 
    DATE_FORMAT(r.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM USED_GOODS_BOARD b
JOIN USED_GOODS_REPLY r 
    ON b.BOARD_ID = r.BOARD_ID
WHERE SUBSTR(b.CREATED_DATE, 1, 7) = '2022-10'
ORDER BY r.CREATED_DATE, b.TITLE;

# 게시판과 댓글에 대해서 BOARD_ID 를 기준으로 JOIN을 진행함.
# 게시글의 댓글이 2022년 10월이기에 BETWEEN을 사용해서 안에 있는 정보들을 가져오기
# 정렬을 문제의 조건에 맞게 설정
# DATE FORMAT에 시간이 포함되어 있으니, DATE_FORMAT() 함수를 사용해 년,월,일만 뜨도록 설정 