SELECT e.ID, e.GENOTYPE, d.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA e
JOIN ECOLI_DATA d 
    ON e.PARENT_ID = d.ID
WHERE (e.GENOTYPE | d.GENOTYPE) = e.GENOTYPE
ORDER BY e.ID;