-- mport the database dump from hbtn_0d_tvshow
SELECT b.name AS genre, count(a.show_id) AS number_of_shows
FROM tv_show_genres a 
LEFT JOIN tv_genres b 
ON a.genre_id = b.id
GROUP BY a.genre_id
ORDER BY 2 DESC;
