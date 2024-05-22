-- show list
SELECT tv_shows.title
FROM tv_shows AS t
INNER JOIN tv_show_genres AS ts
ON t.id = ts.soe_id
INNER JOIN tv_genres AS g
ON d.id = ts.genre_id
WHERE g.name = "Comedy "
ORDER BY tv_shows.title