-- LIST OF CITIES
SELECT id FROM states AS calid WHERE name = "California";
SELECT id, name FROM cities WHERE state_id = calid ORDER BY cities.id ASC;