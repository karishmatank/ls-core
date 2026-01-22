/* Import this file into a PostgreSQL database.
https://raw.githubusercontent.com/launchschool/sql_course_data/master/sql-and-relational-databases/schema-data-and-sql/more-constraints/films2.sql

In the terminal:
createdb films2
curl 'https://raw.githubusercontent.com/launchschool/sql_course_data/master/sql-and-relational-databases/schema-data-and-sql/more-constraints/films2.sql' | psql -d films2
*/

/* Modify all of the columns to be NOT NULL. */

ALTER TABLE films ALTER COLUMN title SET NOT NULL;
ALTER TABLE films ALTER COLUMN "year" SET NOT NULL;
ALTER TABLE films ALTER COLUMN genre SET NOT NULL;
ALTER TABLE films ALTER COLUMN director SET NOT NULL;
ALTER TABLE films ALTER COLUMN duration SET NOT NULL;

/* How does modifying a column to be NOT NULL affect how it is displayed by \d films? */
/* We now see not null in the "Nullable" column of \d */

/* Add a constraint to the table films that ensures that all films have a unique title. */
ALTER TABLE films
ADD CONSTRAINT unique_title UNIQUE (title);

/* Write a SQL statement to remove the constraint added prior. */
ALTER TABLE films
DROP CONSTRAINT unique_title;

/* Add a constraint to films that requires all rows to have a value for title that is at least 1 character long. */
ALTER TABLE films
ADD CONSTRAINT min_title_len CHECK (length(title) >= 1);

/* What error is shown if the constraint created prior is violated? Write a SQL INSERT statement that demonstrates this. */
INSERT INTO films (title, "year", genre, director, duration) VALUES
('', 2000, '', '', 0);

-- I see the following ERROR:  new row for relation "films" violates check constraint "min_title_len"

/* Write a SQL statement to remove the constraint added */
ALTER TABLE films
DROP CONSTRAINT min_title_len;

/* Add a constraint to the table films that ensures that all films have a year between 1900 and 2100. */
ALTER TABLE films
ADD CONSTRAINT year_range CHECK ("year" BETWEEN 1900 AND 2100);

/* Add a constraint to films that requires all rows to have a value for director that is at least 
3 characters long and contains at least one space character (). */
ALTER TABLE films
ADD CONSTRAINT director_name CHECK (length(director) >= 3 AND director ilike '% %');

-- Further exploration
ALTER TABLE films
ADD CONSTRAINT director_name CHECK (length(director) >= 3 AND director ~ '^[a-zA-Z]+ [a-zA-Z]+$');

/* Write an UPDATE statement that attempts to change the director for "Die Hard" to "Johnny". 
Show the error that occurs when this statement is executed. */

UPDATE films
SET director = 'Johnny'
WHERE title = 'Die Hard';

-- ERROR:  new row for relation "films" violates check constraint "director_name"

/* List three ways to use the schema to restrict what values can be stored in a column. */
/* 
1. Add a constraint, such as a check constraint or a not null constraint
2. Specify a data type that restricts values of other data types from being added
3. (Apparently not null is a separate number in the solution, so we'll stick with the two above)
*/