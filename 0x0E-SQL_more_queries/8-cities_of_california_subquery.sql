-- LIST OF CITIES
SELECT id, name FROM cities WHERE state_id IN (SELECT id FROM states AS calid WHERE name = "California") ORDER BY cities.id ASC;