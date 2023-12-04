SELECT DISTINCT u.name as name, SUM(rr.likes_count) as total_likes FROM
#SELECT DISTINCT u.name as name, r.id, rr.id, rr.parent_id, rr.likes_count FROM
user u JOIN review r on r.user_id = u.id
JOIN review rr on rr.parent_id = r.id
GROUP BY name, r.id
ORDER BY total_likes DESC
#WHERE u.id = 11 and r.id = 15
LIMIT 10;