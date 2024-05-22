-- LIST OF ALLCITIES
SELECT cities.id, cities.name, states.name
WHERE cities.state_id = states.id
ORDER BY cities.id;