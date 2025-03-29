SELECT e.ID, e.GENOTYPE, d.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA e
JOIN ECOLI_DATA d 
    ON e.PARENT_ID = d.ID
WHERE (e.GENOTYPE | d.GENOTYPE) = e.GENOTYPE
ORDER BY e.ID;

# 문제 풀이
# 부모와 자식 관계를 설정하는 부분에서 자기 자신을 JOIN하는 연산이 필요해보였기에, 자기 자신과 PARENT_ID를 기준으로 JOIN 하였다.
# 형질포함을 확인하기 위해 BITWISE OR (|) 연산을 사용해 자식 개체가 부모의 형질을 포함하는지 확인했다.
# 결과 출력에 GENOTYPE을 PARENT_GENOTYPE으로 나오도록 별칭을 해주었고, 
# 마지막에 GROUP BY를 사용하고, 아무것도 명시하지 않았을 때 오름차순이 나오기에 문제의 조건에 맞게 ID를 기준으로 오름차순하였다. 
