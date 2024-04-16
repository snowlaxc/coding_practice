-- 코드를 작성해주세요
SELECT concat(max(IFNULL(LENGTH, "0")), "cm") AS MAX_LENGTH
FROM FISH_INFO