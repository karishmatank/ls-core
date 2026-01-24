/* Import from URL:
https://raw.githubusercontent.com/launchschool/sql_course_data/master/sql-and-relational-databases/relational-data-and-joins/one-to-many-relationships/one-to-many.sql

createdb one_to_many
curl 'https://raw.githubusercontent.com/launchschool/sql_course_data/master/sql-and-relational-databases/relational-data-and-joins/one-to-many-relationships/one-to-many.sql' | psql -d one_to_many
*/

/* Write a SQL statement to add the following call data to the database:

when	duration	first_name	last_name	number
2016-01-18 14:47:00	632	William	Swift	7204890809
*/

-- INSERT INTO contacts (first_name, last_name, "number") VALUES
-- ('William', 'Swift', '7204890809');
-- EDIT: Make sure you look at the contacts list first! This contact was already in contacts!

INSERT INTO calls ("when", duration, contact_id) VALUES
('2016-01-18 14:47:00', 632, 6);

/* Write a SQL statement to retrieve the call times, duration, and first name for all calls not made to William Swift.
*/

SELECT calls."when", calls.duration, contacts.first_name
FROM calls
INNER JOIN contacts ON calls.contact_id = contacts.id
WHERE contacts.id != 6;

/* Write SQL statements to add the following call data to the database:

when	duration	first_name	last_name	number
2016-01-17 11:52:00	175	Merve	Elk	6343511126
2016-01-18 21:22:00	79	Sawa	Fyodorov	6125594874
*/

INSERT INTO contacts (first_name, last_name, "number") VALUES
('Merve', 'Elk', '6343511126'),
('Sawa', 'Fyodorov', '6125594874');

INSERT INTO calls ("when", duration, contact_id) VALUES
('2016-01-17 11:52:00', 175, 27),
('2016-01-18 21:22:00', 79, 28);

/* Add a constraint to contacts that prevents a duplicate value being added in the column number. */
ALTER TABLE contacts
ADD CONSTRAINT unique_number UNIQUE (number);

/* Write a SQL statement that attempts to insert a duplicate number for a new contact but fails. What error is shown?
*/
INSERT INTO contacts (first_name, last_name, "number") VALUES
('Merve', 'Elk', '6343511126');
-- ERROR:  duplicate key value violates unique constraint "unique_number"

/* Draw a conceptual-level entity-relationship diagram for the data we've been working with in this assignment. */

/*
Hard to draw out on here, but there's a one to many relationship:
- A contact can make many calls, modality is 0 I guess? (we can I guess have a contact that hasn't had any calls)
- One call can only have one contact, modality is 1 (call must have a contact)
*/