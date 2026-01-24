/* Create a database to store information related to a workshop */
CREATE DATABASE workshop;

/* One table should be called devices. This table should have columns that meet the following specifications:

Includes a primary key called id that is auto-incrementing.
A column called name, that can contain a String. It cannot be NULL.
A column called created_at that lists the date this device was created. It should be of type timestamp and 
it should also have a default value related to when a device is created.

In the workshop, we have several devices, and each device should have many different parts. These parts are unique 
to each device, so one device can have various parts, but those parts won't be used in any other device. 
Make a table called parts that reflects the information listed above. Table parts should have the following columns that 
meet the following specifications:

An id which auto-increments and acts as the primary key
A part_number. This column should be unique and not null.
A foreign key column called device_id. This will be used to associate various parts with a device.
*/

CREATE TABLE devices (
  id serial PRIMARY KEY,
  "name" text NOT NULL,
  created_at timestamp DEFAULT NOW() -- Can also use CURRENT_TIMESTAMP instead of NOW()
);

CREATE TABLE parts (
  id serial PRIMARY KEY,
  part_number integer UNIQUE NOT NULL,
  device_id integer NOT NULL REFERENCES devices (id)
);

/* Add in two different devices. One should be named, "Accelerometer". The other should be named, "Gyroscope".

The first device should have 3 parts (this is grossly simplified). 
The second device should have 5 parts. The part numbers may be any number between 1 and 10000. 
There should also be 3 parts that don't belong to any device yet.
*/
INSERT INTO devices ("name") VALUES ('Accelerometer'), ('Gyroscope');

-- I need to relax the not null constraint I set prior to allow for parts that don't belong to any device yet
ALTER TABLE parts
ALTER COLUMN device_id DROP NOT NULL;

-- I got the part numbers below from the solution
INSERT INTO parts (part_number, device_id) VALUES
(12, 1),
(14, 1),
(16, 1),
(31, 2),
(33, 2),
(35, 2),
(37, 2),
(39, 2),
(50, NULL),
(54, NULL),
(58, NULL);

/* Write an SQL query to display all devices along with all the parts that make them up. 
We only want to display the name of the devices. Its parts should only display the part_number.

Expected output:
     name      | part_number
---------------+-------------
 Accelerometer |          12
 Accelerometer |          14
 Accelerometer |          16
 Gyroscope     |          31
 Gyroscope     |          33
 Gyroscope     |          35
 Gyroscope     |          37
 Gyroscope     |          39
(8 rows)
*/

SELECT devices.name, parts.part_number
FROM devices
INNER JOIN parts ON devices.id = parts.device_id;

/* We want to grab all parts that have a part_number that starts with 3. Write a SELECT query to get this information. 
This table may show all attributes of the parts table. */
SELECT *
FROM parts
WHERE part_number / 10 = 3;

/*Solution temporarily converts part_number to text to check whether it begins with 3:

SELECT * FROM parts WHERE part_number::text LIKE '3%';

An earlier problem said part numbers have to be between 1 and 10000. In that case, my where clause above only works
if IDs are between 10 and 99! So my way will break easily if we add more diverse part numbers.
*/

/* Write an SQL query that returns a result table with the name of each device in our database together with the 
number of parts for that device. */
SELECT devices.name, count(parts.part_number)
FROM devices
INNER JOIN parts ON devices.id = parts.device_id
GROUP BY devices.name;

/* Note: solution uses left outer join because we may want to reflect devices that have no parts */

/* Alter the SQL query above so that we get a result table that looks like the following. 
name          | count
--------------+-------
Gyroscope     |     5
Accelerometer |     3
(2 rows)
*/

SELECT devices.name, count(parts.part_number)
FROM devices
LEFT JOIN parts ON devices.id = parts.device_id
GROUP BY devices.name
ORDER BY devices.name DESC;


/* Write two SQL queries:

One that generates a listing of parts that currently belong to a device.
part_number | device_id
------------+-----------
         12 |         1
         14 |         1
         16 |         1
         31 |         2
         33 |         2
         35 |         2
         37 |         2
         39 |         2
(8 rows)

One that generates a listing of parts that don't belong to a device.
part_number | device_id
------------+-----------
         50 |
         54 |
         58 |
(3 rows)

Do not include the id column in your queries.
*/

SELECT part_number, device_id
FROM parts
WHERE device_id IS NOT NULL;

SELECT part_number, device_id
FROM parts
WHERE device_id IS NULL;

/* We now insert more data:
INSERT INTO devices (name) VALUES ('Magnetometer');
INSERT INTO parts (part_number, device_id) VALUES (42, 3);

Assuming nothing about the existing order of the records in the database, 
write a SQL statement that will return the name of the oldest device from our devices table.
*/
SELECT "name"
FROM devices
ORDER BY created_at
LIMIT 1;

/* What do you think would happen if we had two devices with the same created_at value that happened to be 
the oldest timestamp? How might this affect what we can infer from the data we get when using a LIMIT clause? */
/* In that case, we'll get an arbitrary result back. We'll get one of those rows, but not necessarily the one we expected. 
We should probably sort by another column as well, such as alphabetically by name, if that's relevant to the answer 
we want back. */

/* We've realized that the last two parts we're using for device number 2, "Gyroscope", actually belong to an "Accelerometer". 
Write an SQL statement that will associate the last two parts from our parts table with an "Accelerometer" instead of 
a "Gyroscope". */
UPDATE parts
SET device_id = 1
WHERE part_number in (37, 39);

/* What if we wanted to set the part with the smallest part_number to be associated with "Gyroscope"? 
How would we go about doing that? */
UPDATE parts
SET device_id = 2
WHERE part_number = 12;

-- Or, without too many hardcodes:

UPDATE parts
SET device_id = (
  SELECT id from devices where "name" = 'Gyroscope'
)
WHERE part_number = (
  SELECT min(part_number) from parts
);

/* Delete any data related to "Accelerometer", this includes the parts associated with an Accelerometer. */

-- I want to take advantage of on delete cascade, but we don't currently have that with the foreign key constraint
-- So I'll drop the constraint, then add it again, and then delete the data
ALTER TABLE parts
DROP CONSTRAINT parts_device_id_fkey;

ALTER TABLE parts
ADD FOREIGN KEY (device_id) REFERENCES devices (id) ON DELETE CASCADE;

-- This will now delete the device as well as its parts
DELETE FROM devices
WHERE name = 'Accelerometer';