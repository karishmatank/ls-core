/*  Create a new database called residents using the PostgreSQL command line tools. */
-- createdb residents

/* 
Load file at the link into the database created in #1.
Link is https://raw.githubusercontent.com/launchschool/sql_course_data/master/sql-and-relational-databases/schema-data-and-sql/more-single-table-queries/residents_with_data.sql
*/

-- curl 'https://raw.githubusercontent.com/launchschool/sql_course_data/master/sql-and-relational-databases/schema-data-and-sql/more-single-table-queries/residents_with_data.sql' | psql -d residents

/* Write a SQL query to list the ten states with the most rows in the people table in descending order. */

SELECT "state", count(id) AS count
FROM people
GROUP BY "state"
ORDER BY count DESC
LIMIT 10;

/* Write a SQL query that lists each domain used in an email address in the people table 
and how many people in the database have an email address containing that domain. 
Domains should be listed with the most popular first.
*/

SELECT
  substring(email from position('@' in email) + 1 for (length(email) - position('@' in email) + 1)) AS domain,
  count(email) AS count
FROM people
GROUP BY domain
ORDER BY count DESC; 

-- I realized later that I didn't need the succeeding "for" as it's optional as per the documentation:

SELECT
  substring(email from position('@' in email) + 1) AS domain,
  count(email) AS count
FROM people
GROUP BY domain
ORDER BY count DESC; 

/* Write a SQL statement that will delete the person with ID 3399 from the people table.*/

DELETE FROM people
WHERE id = 3399;

/* Write a SQL statement that will delete all users that are located in the state of California (CA).*/

DELETE FROM people
WHERE state = 'CA';

/* Write a SQL statement that will update the given_name values to be all uppercase for all users with an
 email address that contains teleworm.us */

UPDATE people
SET given_name = upper(given_name)
WHERE email ilike '%teleworm.us';

/* Write a SQL statement that will delete all rows from the people table. */
DELETE FROM people;