-- sqlite3 library.db < initial-data.sql

-- Countries
INSERT INTO country (id, name) VALUES (1, 'India');
INSERT INTO country (id, name) VALUES (2, 'England');
INSERT INTO country (id, name) VALUES (3, 'United States');
INSERT INTO country (id, name) VALUES (4, 'Germany');
INSERT INTO country (id, name) VALUES (5, 'France');
INSERT INTO country (id, name) VALUES (6, 'Norway');

-- Authors
INSERT INTO author (id, country_id, name) VALUES (1, 1, 'Rabindranath Tagore');
INSERT INTO author (id, country_id, name) VALUES (2, 1, 'Mahatma Gandhi');
INSERT INTO author (id, country_id, name) VALUES (3, 2, 'Charles Dickens');
INSERT INTO author (id, country_id, name) VALUES (4, 3, 'Jack London');
INSERT INTO author (id, country_id, name) VALUES (5, 3, 'Uptron Sinclare');
INSERT INTO author (id, country_id, name) VALUES (6, 4, 'Thomas Mann');
INSERT INTO author (id, country_id, name) VALUES (7, 5, 'Victor Hugo');
INSERT INTO author (id, country_id, name) VALUES (8, 6, 'Knut Hamsun');