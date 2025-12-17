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