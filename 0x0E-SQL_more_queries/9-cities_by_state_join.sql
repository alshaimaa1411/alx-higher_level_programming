-- LIST OF ALLCITIES
SELECT hbtn_0d_usa.cities.id, hbtn_0d_usa.cities.name, hbtn_0d_usa.states.name
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;