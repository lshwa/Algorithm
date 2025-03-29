SELECT b.TITLE, b.BOARD_ID, r.REPLY_ID, r.WRITER_ID, r.CONTENTS, 
    DATE_FORMAT(r.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM USED_GOODS_BOARD b
JOIN USED_GOODS_REPLY r 
    ON b.BOARD_ID = r.BOARD_ID
WHERE SUBSTR(b.CREATED_DATE, 1, 7) = '2022-10'
ORDER BY r.CREATED_DATE, b.TITLE;

# 게시판과 댓글에 대해서 BOARD_ID 를 기준으로 JOIN을 진행함.
# 게시글의 댓글이 2022년 10월이기에 처음에는 BETWEEN 을 활용하려고 했지만 계속 오답이 나오고, 
# 이부분에는 문제가 없다고 생각하여, 여기 부분을 SUBSTR을 활용해 날짜 형식에 맞춰 10월까지인지만 나오게 하고
# 그 뒷부분은 무시하고 년도와 월만 일치시킨 다음에 비교 진행 -> 문제 없이 해결 완료
# 정렬을 문제의 조건에 맞게 설정
# DATE FORMAT에 시간이 포함되어 있으니, DATE_FORMAT() 함수를 사용해 년,월,일만 뜨도록 설정 
