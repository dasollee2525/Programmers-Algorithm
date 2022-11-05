-- 코드를 입력하세요
SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, "%Y-%m-%d")
FROM MEMBER_PROFILE P JOIN REST_REVIEW R
ON P.MEMBER_ID = R.MEMBER_ID
WHERE P.MEMBER_ID IN (SELECT MEMBER_ID
                        FROM REST_REVIEW
                        GROUP BY MEMBER_ID
                        HAVING count(member_id) = (SELECT COUNT(REVIEW_TEXT) AS 'NUM'
                                FROM REST_REVIEW
                                GROUP BY MEMBER_ID
                                ORDER BY NUM DESC
                                LIMIT 1))
ORDER BY 3 ASC, 2 ASC;
