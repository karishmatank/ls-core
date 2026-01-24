/* Import the file at the link below into a database
https://raw.githubusercontent.com/launchschool/sql_course_data/master/sql-and-relational-databases/relational-data-and-joins/working-with-multiple-tables/theater_full.sql
*/

/* createdb theater_full
   curl 'https://raw.githubusercontent.com/launchschool/sql_course_data/master/sql-and-relational-databases/relational-data-and-joins/working-with-multiple-tables/theater_full.sql' | psql -d theater_full
*/

/* Write a query that determines how many tickets have been sold. */
SELECT count(id) FROM tickets;

/* Write a query that determines how many different customers purchased tickets to at least one event. */
SELECT count(DISTINCT customer_id) FROM tickets;

/* Write a query that determines what percentage of the customers in the database have purchased a ticket 
to one or more of the events. */
SELECT 
  round(count(distinct t.customer_id) * 100 / count(distinct c.id)::decimal, 2) as percent
FROM customers c
LEFT JOIN tickets t ON c.id = t.customer_id;

/* Write a query that returns the name of each event and how many tickets were sold for it, 
in order from most popular to least popular. */
SELECT
  events.name as "name",
  count(tickets.id) as popularity
FROM events
LEFT JOIN tickets ON events.id = tickets.event_id
GROUP BY "name"
ORDER BY popularity DESC;

/* Write a query that returns the user id, email address, and number of events for all customers 
that have purchased tickets to three events. */
SELECT
  customers.id,
  customers.email,
  count(distinct tickets.event_id)
FROM customers
LEFT JOIN tickets on tickets.customer_id = customers.id
GROUP BY customers.id, customers.email
HAVING count(distinct tickets.event_id) = 3
ORDER BY customers.id;
-- NOTE: Inner join would have been the better choice above for intent.
-- "it more clearly shows that we're not interested in non-matching customers or tickets"

/* Write a query to print out a report of all tickets purchased by the customer with the email address 
'gennaro.rath@mcdermott.co'. 
The report should include the event name and starts_at and the seat's section name, row, and seat number.
*/

SELECT events.name, events.starts_at, sections.name as section, seats.row, seats.number as seat
FROM events
INNER JOIN tickets ON tickets.event_id = events.id
LEFT JOIN customers ON tickets.customer_id = customers.id
LEFT JOIN seats ON tickets.seat_id = seats.id
LEFT JOIN sections ON seats.section_id = sections.id
WHERE customers.email = 'gennaro.rath@mcdermott.co';
-- We also could have just used inner joins for all of these too