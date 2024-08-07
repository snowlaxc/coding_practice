WITH MAX_FISH AS (
    SELECT FISH_TYPE, MAX(LENGTH) AS MAX_LENGTH
    FROM FISH_INFO
    GROUP BY FISH_TYPE
)

SELECT I.ID, N.FISH_NAME, I.LENGTH
FROM FISH_INFO I
    JOIN FISH_NAME_INFO N ON I.FISH_TYPE = N.FISH_TYPE
    JOIN MAX_FISH M ON I.FISH_TYPE = M.FISH_TYPE AND I.LENGTH = M.MAX_LENGTH
ORDER BY ID ASC;