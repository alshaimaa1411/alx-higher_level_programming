-- show list
SELECT tv_shows.title
FROM tv_shows AS t
INNER JOIN tv_show_genres AS ts
ON t.id = ts.show_id
INNER JOIN tv_genres AS g
ON g.id = ts.genre_id
WHERE g.name = "Comedy "
ORDER BY tv_shows.title