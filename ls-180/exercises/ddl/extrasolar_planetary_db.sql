/* To get started, first create a postgresql database named "extrasolar", and then create two tables in the database as follows:

stars table

id: a unique serial number that auto-increments and serves as a primary key for this table.
name: the name of the star,e,g., "Alpha Centauri A". Allow room for 25 characters. Must be unique and non-null.
distance: the distance in light years from Earth. Define this as a whole number (e.g., 1, 2, 3, etc) that must be 
non-null and greater than 0.
spectral_type: the spectral type of the star: O, B, A, F, G, K, and M. Use a one character string.
companions: how many companion stars does the star have? A whole number will do. Must be non-null and non-negative.

planets table

id: a unique serial number that auto-increments and serves as a primary key for this table.
designation: a single alphabetic character that uniquely identifies the planet in its star system ('a', 'b', 'c', etc.)
mass: estimated mass in terms of Jupiter masses; use an integer for this value.
*/

CREATE DATABASE extrasolar; -- createdb extrasolar

-- Connect to database: psql -d extrasolar

CREATE TABLE stars (
  id serial PRIMARY KEY,
  "name" varchar(25) UNIQUE NOT NULL,
  distance integer NOT NULL,
  spectral_type char(1),
  companions integer NOT NULL,
  CHECK (distance > 0),
  CHECK (companions >= 0)
);

-- Note: We can just add the checks to the column definition lines i.e. 
-- distance integer NOT NULL CHECK (distance > 0)

CREATE TABLE planets (
  id serial PRIMARY KEY,
  designation char(1) UNIQUE,
  mass integer
);

/* Add a star_id column to the planets table; this column will be used to relate each planet in the planets table 
to its home star in the stars table. 
Make sure the column is defined in such a way that it is required and must have a value that is present as an id 
in the stars table */

ALTER TABLE planets
ADD COLUMN star_id integer NOT NULL REFERENCES stars (id);

/* Modify the star table's "name" column so that it allows star names as long as 50 characters. */
ALTER TABLE stars
ALTER COLUMN "name" TYPE varchar(50);

/* Assume the stars table already contains one or more rows of data. What will happen when you try to run the above command? 
To test this, revert the modification and add a row or two of data:
ALTER TABLE stars
ALTER COLUMN name TYPE varchar(25);

INSERT INTO stars (name, distance, spectral_type, companions)
           VALUES ('Alpha Centauri B', 4, 'K', 3);

ALTER TABLE stars
ALTER COLUMN name TYPE varchar(50);
*/

/* My guess is that it should work fine, as we are increasing the possible number of characters.
It perhaps wouldn't work if we were decreasing character count. */


/* Modify the distance column in the stars table so that it allows fractional light years to any degree of precision required. */
ALTER TABLE stars
ALTER COLUMN distance TYPE numeric;

-- NOTE: Use numeric instead of float. Numeric is designed for exact decimal values, whereas float is an approximate type

/* Assume the stars table already contains one or more rows of data. What will happen when you try to run the above command? 
To test this, revert the modification and add a row or two of data:
ALTER TABLE stars
ALTER COLUMN distance TYPE integer;

INSERT INTO stars (name, distance, spectral_type, companions)
           VALUES ('Alpha Orionis', 643, 'M', 9);

ALTER TABLE stars
ALTER COLUMN distance TYPE numeric;
*/

/* My guess is that this will work correctly. Again, we are going from a data type of less precision to more precision,
so that means 643 will not be an issue. It would be an issue if we had 643.1 and we wanted to go from numeric to integer. */

/* 
The spectral_type column in the stars table is currently defined as a one-character string 
that contains one of the following 7 values: 'O', 'B', 'A', 'F', 'G', 'K', and 'M'. 
However, there is currently no enforcement on the values that may be entered. 
Add a constraint to the table stars that will enforce the requirement that a row must hold one 
of the 7 listed values above. Also, make sure that a value is required for this column.
*/
ALTER TABLE stars
ADD CHECK (spectral_type IN ('O', 'B', 'A', 'F', 'G', 'K', 'M'));

ALTER TABLE stars
ALTER COLUMN spectral_type
SET NOT NULL;

/* Assume the stars table contains one or more rows that are missing a spectral_type value, or that have an illegal value. 
What will happen when you try to alter the table schema? 
How would you go about adjusting the data to work around this problem. */

/* If we have missing or illegal values, the constraints won't be added, as we'll get errors that we can't place those 
constraints on the table / column because of those invalid values currently in the table. 
To solve for this, we would need to adjust the values in the table currently such that they have valid values, such as 
setting values for rows where the column value is currently NULL or replacing chars in rows where the char is now invalid.
We may also decide to delete those rows if the data is invalid.
*/

/* Modify the stars table to remove the CHECK constraint on the spectral_type column, 
and then modify the spectral_type column so it becomes an enumerated type that restricts it to one of the following 7 values: 
'O', 'B', 'A', 'F', 'G', 'K', and 'M'. */
ALTER TABLE stars
DROP CONSTRAINT stars_spectral_type_check;

CREATE TYPE spectral_values AS ENUM ('O', 'B', 'A', 'F', 'G', 'K', 'M');

ALTER TABLE stars
ALTER COLUMN spectral_type TYPE spectral_values USING spectral_type::spectral_values;
-- If you don't include USING, you'll get an error

/* Modify the mass column in the planets table so that it allows fractional masses to any degree of precision required. 
In addition, make sure the mass is required and positive. 
While we're at it, also make the designation column required.
*/

ALTER TABLE planets
ALTER COLUMN mass TYPE numeric,
ADD CHECK (mass > 0),
ALTER COLUMN mass SET NOT NULL,
ALTER COLUMN designation SET NOT NULL;

/* Add a semi_major_axis column for the semi-major axis of each planet's orbit; 
the semi-major axis is the average distance from the planet's star as measured in astronomical units 
(1 AU is the average distance of the Earth from the Sun). 
Use a data type of numeric, and require that each planet have a value for the semi_major_axis. */
ALTER TABLE planets
ADD COLUMN semi_major_axis numeric NOT NULL;

/* Assume the planets table already contains one or more rows of data. What will happen when you try to run 
the above command? What will you need to do differently to obtain the desired result? */

/* We'll get an error because of the not null constraint, because we're saying the column can't have 
any nulls, yet the existing data would have nulls since we don't have any data for that column yet.
I think what we'll need to do differently is specify a default value such that existing data's values for the 
new column will have that default value that we can go in and change as desired.
Or, alternatively, we can drop the not null constraint for now, add the column, update the table to add in
values for the column for existing rows, and then add the not null constraint back.
*/

/* Someday in the future, technology will allow us to start observing the moons of extrasolar planets. 
At that point, we're going to need a moons table in our extrasolar database. For this exercise, 
your task is to add that table to the database. The table should include the following data:

id: a unique serial number that auto-increments and serves as a primary key for this table.
designation: the designation of the moon. We will assume that moon designations will be numbers, 
with the first moon discovered for each planet being moon 1, the second moon being moon 2, etc. The designation is required.
semi_major_axis: the average distance in kilometers from the planet when a moon is farthest from its 
corresponding planet. This field must be a number greater than 0, but is not required; 
it may take some time before we are able to measure moon-to-planet distances in extrasolar systems.
mass: the mass of the moon measured in terms of Earth Moon masses. This field must be a 
numeric value greater than 0, but is not required.

Make sure you also specify any foreign keys necessary to tie each moon to other rows in the database.
*/
CREATE TABLE moons (
  id serial PRIMARY KEY,
  designation integer CHECK (designation > 0),
  semi_major_axis numeric CHECK (semi_major_axis > 0),
  mass numeric CHECK (mass > 0),
  planet_id integer NOT NULL REFERENCES planets (id)
);

/* Note:
1. I originally used serial as the data type for designation. I realized after looking at the solution that we want
numbers per planet (per planet label), not overall in the table. So we should use the integer data type instead 
and make sure the integer is not <= 0.
2. I originally did not include the not null constraint for planet_id. We should though, as we want each moon to be
associated with a planet 
*/

/* We can make a backup of a database by using the below command from the terminal:
$ pg_dump --inserts extrasolar > extrasolar.dump.sql
*/