SELECT ROUTE, 
    CONCAT(ROUND(SUM(D_BETWEEN_DIST),1),'km') AS TOTAL_DISTANCE, 
    CONCAT(ROUND(AVG(D_BETWEEN_DIST),2),'km') AS AVERAGE_DISTANCE
FROM SUBWAY_DISTANCE
GROUP BY ROUTE
ORDER BY SUM(D_BETWEEN_DIST) DESC;

# CONCAT을 통해 뒤에 'km' 단위 추가
# ROUND를 통해 문제의 조건에 맞게 소수점 자리에서 반올림
# SUM, AVG 집계함수 사용해서 총 누계거리와 평균 역 사이의 거리 구하기
# 여기서 중요한 점, 개별역에 대한 누적거리로 계산될 가능성이 있기 때문에 총 누계 거리를 역 사이의 거리의 총합으로 대체 
# ORDER BY는 문자열로 안되기 때문에 NUMBER TYPE인 D_BETWEEN_DIST 로 해야함.
# 내림차순 정렬 