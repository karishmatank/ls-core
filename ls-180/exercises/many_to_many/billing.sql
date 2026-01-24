/*
createdb billing
psql -d billing
*/

/* Create a customers table */
CREATE TABLE customers (
  id serial PRIMARY KEY,
  name text NOT NULL,
  payment_token char(8) UNIQUE NOT NULL CHECK (payment_token ~ '^[A-Z]+$' AND length(payment_token) = 8)
);

-- Note: You do need to check the length, as even though char(8) pads with spaces, it isn't padded when doing the check.
-- A more concise way to write would have been payment_token ~ '^[A-Z]{8}$'

CREATE TABLE services (
  id serial PRIMARY KEY,
  description text NOT NULL,
  price numeric(10,2) NOT NULL CHECK (price >= 0)
);

INSERT INTO customers (name, payment_token) VALUES
('Pat Johnson', 'XHGOAHEQ'),
('Nancy Monreal', 'JKWQPJKL'),
('Lynn Blake', 'KLZXWEEE'),
('Chen Ke-Hua', 'KWETYCVX'),
('Scott Lakso', 'UUEAPQPS'),
('Jim Pornot', 'XKJEYAZA');

INSERT INTO services (description, price) VALUES
('Unix Hosting', 5.95),
('DNS', 4.95),
('Whois Registration', 1.95),
('High Bandwidth', 15.00),
('Business Support', 250.00),
('Dedicated Hosting', 50.00),
('Bulk Email', 250.00),
('One-to-one Training', 999.00);

CREATE TABLE customers_services (
  id serial PRIMARY KEY,
  customer_id integer NOT NULL REFERENCES customers (id) ON DELETE CASCADE,
  service_id integer NOT NULL REFERENCES services (id),
  UNIQUE (customer_id, service_id)
);

INSERT INTO customers_services (customer_id, service_id) VALUES
(1, 1),
(1, 2),
(1, 3),
(3, 1),
(3, 2),
(3, 3),
(3, 4),
(3, 5),
(4, 1),
(4, 4),
(5, 1),
(5, 2),
(5, 6),
(6, 1),
(6, 6),
(6, 7);

/* Write a query to retrieve the customer data for every customer who currently subscribes to at least one service. */
SELECT DISTINCT customers.*
FROM customers
INNER JOIN customers_services ON customers.id = customers_services.customer_id;

/* Write a query to retrieve the customer data for every customer who does not currently subscribe to any services. */
SELECT customers.*
FROM customers
LEFT JOIN customers_services ON customers.id = customers_services.customer_id
WHERE customers_services.customer_id IS NULL;

/* Can you write a query that displays all customers with no services and all services that currently 
don't have any customers? The output should look like this:
 id |     name      | payment_token | id |     description     | price
----+---------------+---------------+----+---------------------+--------
  2 | Nancy Monreal | JKWQPJKL      |    |                     |
    |               |               |  8 | One-to-one Training | 999.00
(2 rows)
*/

SELECT customers.*, services.*
FROM customers
FULL OUTER JOIN customers_services ON customers.id = customers_services.customer_id
FULL OUTER JOIN services ON services.id = customers_services.service_id
WHERE services.id IS NULL OR customers.id IS NULL;

/* Using RIGHT OUTER JOIN, write a query to display a list of all services that are not currently in use. 
Your output should look like this:
 description
-------------
 One-to-one Training
(1 row)
*/

SELECT services.description
FROM customers_services
RIGHT JOIN services ON customers_services.service_id = services.id
WHERE customers_services.customer_id IS NULL;

/* Write a query to display a list of all customer names together with a comma-separated list 
of the services they use. Your output should look like this:
     name      |                                services
---------------+-------------------------------------------------------------------------
 Pat Johnson   | Unix Hosting, DNS, Whois Registration
 Nancy Monreal |
 Lynn Blake    | DNS, Whois Registration, High Bandwidth, Business Support, Unix Hosting
 Chen Ke-Hua   | High Bandwidth, Unix Hosting
 Scott Lakso   | DNS, Dedicated Hosting, Unix Hosting
 Jim Pornot    | Unix Hosting, Dedicated Hosting, Bulk Email
(6 rows)
*/

SELECT customers.name, string_agg(services.description, ', ')
FROM customers
LEFT JOIN customers_services ON customers_services.customer_id = customers.id
LEFT JOIN services ON customers_services.service_id = services.id
GROUP BY customers.id
ORDER BY customers.id;

/* Modify the above command so it looks like the below
     name      |    description
---------------+--------------------
 Chen Ke-Hua   | High Bandwidth
               | Unix Hosting
 Jim Pornot    | Dedicated Hosting
               | Unix Hosting
               | Bulk Email
 Lynn Blake    | Whois Registration
               | High Bandwidth
               | Business Support
               | DNS
               | Unix Hosting
 Nancy Monreal |
 Pat Johnson   | Whois Registration
               | DNS
               | Unix Hosting
 Scott Lakso   | DNS
               | Dedicated Hosting
               | Unix Hosting
(17 rows)
*/

SELECT 
  CASE WHEN 
    lag(customers.name) OVER (ORDER BY customers.name) != customers.name OR
    lag(customers.name) OVER (ORDER BY customers.name) IS NULL
    THEN customers.name
  END as name,
  services.description
FROM customers
LEFT OUTER JOIN customers_services
             ON customer_id = customers.id
LEFT OUTER JOIN services
             ON services.id = service_id
;

/* Write a query that displays the description for every service that is subscribed to by at least 3 customers. 
Include the customer count for each description in the report. The report should look like this:
 description  | count
--------------+-------
 DNS          |     3
 Unix Hosting |     5
(2 rows)
*/
SELECT services.description, count(customers_services.service_id)
FROM services
INNER JOIN customers_services ON services.id = customers_services.service_id
GROUP BY services.description
HAVING count(customers_services.service_id) >= 3;

/* Assuming that everybody in our database has a bill coming due, and that all of them will pay on time, 
write a query to compute the total gross income we expect to receive. */
SELECT sum(price) as gross
FROM services
INNER JOIN customers_services ON customers_services.service_id = services.id;

/* A new customer, 'John Doe', has signed up with our company. His payment token is 'EYODHLCN'. 
Initially, he has signed up for UNIX hosting, DNS, and Whois Registration. 
Create any SQL statement(s) needed to add this record to the database. */
INSERT INTO customers (name, payment_token) VALUES
('John Doe', 'EYODHLCN');

INSERT INTO customers_services (customer_id, service_id) VALUES
(7, 1),
(7, 2),
(7, 3);

/* In separate queries, calculate the amount of expected income from "big ticket" services (those services that cost more than 
$100) and the maximum income the company could achieve if it managed to convince all of its customers to select all of the 
company's big ticket items. */
SELECT sum(services.price)
FROM services
INNER JOIN customers_services ON customers_services.service_id = services.id
WHERE services.price > 100;

-- We have 7 total customers in our database (all but 1 are currently purchasing)
-- We have 3 big ticket services

SELECT sum(price)
FROM services
CROSS JOIN customers
WHERE services.price > 100;

/* Write the necessary SQL statements to delete the "Bulk Email" service and customer "Chen Ke-Hua" from the database. */
DELETE FROM services
WHERE description = 'Bulk Email';

DELETE FROM customers
WHERE name = 'Chen Ke-Hua';

-- These two don't delete service_id = 7 from customers_services, since we didn't set up on delete cascade from that
-- We actually have to do that first before deleting from the services table, otherwise we get an error!
-- So we do the below **FIRST**:
DELETE FROM customers_services
WHERE service_id = 7;