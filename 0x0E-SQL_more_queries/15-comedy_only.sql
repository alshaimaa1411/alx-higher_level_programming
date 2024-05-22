-- show list
SELECT tv_shows.title
FROM tv_shows AS t
LEFT JOIN tv_show_genres AS ts
ON t.id = ts.show_id
LEFT JOIN tv_genres AS g
ON g.id = ts.genre_id
WHERE g.name = "Comedy "
GROUP BY t.title
ORDER BY t.title;