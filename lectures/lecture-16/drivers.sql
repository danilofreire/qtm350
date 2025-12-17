DROP TABLE IF EXISTS drivers;

CREATE TABLE drivers(
    driver_id int,
    driver_name varchar(30),
    nationality varchar(15),
    victories int
);

INSERT INTO drivers VALUES (1, 'Lewis Hamilton','British', 103);

INSERT INTO drivers VALUES (4, 'Fernando Alonso', 'Spanish', 32);

INSERT INTO drivers VALUES (3, 'Sebastian Vettel', 'German', 91);

INSERT INTO drivers VALUES (2, 'Michael Schumacher', 'German', 53);

INSERT INTO drivers VALUES (5, 'Max Verstappen', 'Dutch', 51); 

INSERT INTO drivers VALUES (6, 'Juan Pablo Montoya', 'Colombian', 6);

INSERT INTO drivers VALUES (7, 'Danilo Freire','Brazilian', 10);

SELECT * FROM drivers;

SELECT driver_id, nationality FROM drivers;

SELECT * FROM drivers
WHERE nationality = 'German';

SELECT * FROM drivers
WHERE (nationality = 'Brazilian') OR (nationality = 'German');

SELECT * FROM drivers
WHERE (nationality = 'German') AND (driver_id = 3) ;

SELECT SUM(victories) AS sum_victories,
       COUNT(*) AS num_rows,
       AVG(victories) AS mean_victories,
       MIN(victories) AS min_victories,
       MAX(victories) AS max_victories
FROM drivers;

SELECT driver_name, nationality, victories
FROM drivers
WHERE (nationality = 'German' OR nationality = 'British') AND victories > 50;

SELECT driver_name, victories
FROM drivers
WHERE victories > (SELECT AVG(victories) FROM drivers);

SELECT driver_name, victories FROM drivers
ORDER BY victories ASC;

SELECT nationality,
       SUM(victories) AS sum_victories,
       AVG(victories) AS mean_victories,
       MIN(victories) AS min_victories,
       MAX(victories) AS max_victories
FROM drivers
GROUP BY nationality;

SELECT nationality,
       SUM(victories) AS sum_victories,
       ROUND(AVG(victories), 1) AS mean_victories,
       MIN(victories) AS min_victories,
       MAX(victories) AS max_victories
FROM drivers
GROUP BY nationality;

SELECT nationality,
       SUM(victories) AS sum_victories,
       ROUND(AVG(victories), 1) AS mean_victories,
       MIN(victories) AS min_victories,
       MAX(victories) AS max_victories
FROM drivers
GROUP BY nationality
HAVING SUM(victories) > 50;

SELECT driver_name, nationality, victories
FROM drivers
WHERE (nationality = 'German' OR nationality = 'British') AND victories > 50;

SELECT driver_name, victories
FROM drivers
WHERE victories > (SELECT AVG(victories) FROM drivers);
