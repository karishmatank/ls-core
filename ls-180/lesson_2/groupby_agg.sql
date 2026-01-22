/* Import file into database */
-- createdb films3
-- curl 'https://raw.githubusercontent.com/launchschool/sql_course_data/master/sql-and-relational-databases/schema-data-and-sql/group-by-and-aggregate-functions/films4.sql' | psql -d films3

/* Write SQL statements that will insert the following films into the database:

title	year	genre	director	duration
Wayne's World	1992	comedy	Penelope Spheeris	95
Bourne Identity	2002	espionage	Doug Liman	118
*/

INSERT INTO films (title, "year", genre, director, duration) VALUES
('Wayne''s World', 1992, 'comedy', 'Penelope Spheeris', 95),
('Bourne Identity', 2002, 'espionage', 'Doug Liman', 118);

/* Write a SQL query that lists all genres for which there is a movie in the films table. */

SELECT DISTINCT genre
FROM films;

/* Write a SQL query that returns the same results as the answer for #3, but without using DISTINCT. */
-- Used a hint from LSBot to use group by
SELECT genre
FROM (
  SELECT genre, count(id) as "count_films"
  FROM films
  GROUP BY genre
) as subtable;

-- Edit: I thought I needed to use a subquery here, but turns out it's as simple as the below
-- We don't always need to specify an aggregate function when using group by
SELECT genre
FROM films
GROUP BY genre;

/* Write a SQL query that determines the average duration across all the movies in the films table, 
rounded to the nearest minute. */

SELECT round(avg(duration), 0)
FROM films;

/* Write a SQL query that determines the average duration for each genre in the films table, 
rounded to the nearest minute.
*/

SELECT genre, round(avg(duration), 0)
FROM films
GROUP BY genre;

/* Write a SQL query that determines the average duration of movies for each decade represented in the films table, 
rounded to the nearest minute and listed in chronological order. */

-- This takes advantage of integer division being imprecise to get the decade. 1995 / 10 = 199, 199 * 10 = 1990
SELECT ("year" / 10 * 10) as decade, round(avg(duration), 0) AS avg_duration
FROM films
GROUP BY decade
ORDER BY decade;

/* Write a SQL query that finds all films whose director has the first name John. */
SELECT *
FROM films
WHERE director ilike 'john %';

/* Write a SQL query that will return the following data:
   genre   | count
-----------+-------
 scifi     |     5
 comedy    |     4
 drama     |     2
 espionage |     2
 crime     |     1
 thriller  |     1
 horror    |     1
 action    |     1
(8 rows) */

SELECT genre, count(id) as film_count
FROM films
GROUP BY genre
ORDER BY film_count DESC;

/* Write a SQL query that will return the following data:
 decade |   genre   |                  films
--------+-----------+------------------------------------------
   1940 | drama     | Casablanca
   1950 | drama     | 12 Angry Men
   1950 | scifi     | 1984
   1970 | crime     | The Godfather
   1970 | thriller  | The Conversation
   1980 | action    | Die Hard
   1980 | comedy    | Hairspray
   1990 | comedy    | Home Alone, The Birdcage, Wayne's World
   1990 | scifi     | Godzilla
   2000 | espionage | Bourne Identity
   2000 | horror    | 28 Days Later
   2010 | espionage | Tinker Tailor Soldier Spy
   2010 | scifi     | Midnight Special, Interstellar, Godzilla
(13 rows) */

SELECT ("year" / 10 * 10) as decade, genre, string_agg(title, ', ') as films
FROM films
GROUP BY decade, genre
ORDER BY decade, genre, films;

/* Write a SQL query that will return the following data:

   genre   | total_duration
-----------+----------------
 horror    |            113
 thriller  |            113
 action    |            132
 crime     |            175
 drama     |            198
 espionage |            245
 comedy    |            407
 scifi     |            632
(8 rows) */

SELECT genre, sum(duration) as total_duration
FROM films
GROUP BY genre
ORDER BY total_duration, genre;