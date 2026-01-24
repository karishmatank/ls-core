/* createdb auction */

/* Table set up */
CREATE TABLE bidders (
  id serial PRIMARY KEY,
  name text NOT NULL
);

CREATE TABLE items (
  id serial PRIMARY KEY,
  name text NOT NULL,
  initial_price numeric(6,2) NOT NULL CHECK (initial_price > 0 and initial_price <= 1000),
  sales_price numeric(6,2) CHECK (sales_price > 0 and sales_price <= 1000)
);

CREATE TABLE bids (
  id serial PRIMARY KEY,
  bidder_id integer NOT NULL REFERENCES bidders (id) ON DELETE CASCADE,
  item_id integer NOT NULL REFERENCES items (id) ON DELETE CASCADE,
  amount numeric(6,2) NOT NULL CHECK (amount > 0 and amount <= 1000)
);

CREATE INDEX ON bids (bidder_id, item_id);

/* 
-- Copy data for bidders from the csv file to the bidders table
\copy bidders FROM 'bidders.csv' WITH HEADER CSV

-- Copy data for items from the csv file to the items table
\copy items FROM 'items.csv' WITH HEADER CSV

-- Copy data for bids from the csv file to the bids table
\copy bids FROM 'bids.csv' WITH HEADER CSV
*/

/* Write a SQL query that shows all items that have had bids put on them. 
Use the logical operator IN for this exercise, as well as a subquery. 

Here is the expected output:
 Bid on Items
---------------
 Video Game
 Outdoor Grill
 Painting
 Tent
 Vase
(5 rows)
*/

SELECT name as "Bid on Items"
FROM items
WHERE id in (
  SELECT DISTINCT item_id FROM bids
);

/* Write a SQL query that shows all items that have not had bids put on them. 
Use the logical operator NOT IN for this exercise, as well as a subquery.

Here is the expected output:
 Not Bid On
------------
 Television
(1 row)
*/

SELECT name as "Not Bid On"
FROM items
WHERE ID not in (
  SELECT DISTINCT item_id FROM bids
);

/* Write a SELECT query that returns a list of names of everyone who has bid in the auction. 
While it is possible (and perhaps easier) to do this with a JOIN clause, we're going to do things differently: 
use a subquery with the EXISTS clause instead. 

Here is the expected output:
      name
-----------------
 Alison Walker
 James Quinn
 Taylor Williams
 Alexis Jones
 Gwen Miller
 Alan Parker
(6 rows)
*/

-- Without EXISTS to start
SELECT name
FROM bidders
WHERE id in (
  SELECT bidder_id FROM bids
);

-- With EXISTS (didn't get this one)
SELECT name
FROM bidders
WHERE EXISTS (
  SELECT 1 FROM bids WHERE bids.bidder_id = bidders.id
);

-- With a join (further exploration)
SELECT DISTINCT bidders.name
FROM bidders
INNER JOIN bids ON bidders.id = bids.bidder_id;

/* Write an SQL query that finds the largest number of bids from an individual bidder.

For this exercise, you must use a subquery to generate a result table (or transient table), and then query that table 
for the largest number of bids.

Your output should look like this:
  max
------
    9
(1 row)
*/

SELECT max(bid_count)
FROM (
  SELECT bidder_id, count(id) as bid_count
  FROM bids
  GROUP BY bidder_id
) as bids_counts;

/* For this exercise, use a scalar subquery to determine the number of bids on each item. 
The entire query should return a table that has the name of each item along with the number of bids on an item.

Here is the expected output:
    name      | count
--------------+-------
Video Game    |     4
Outdoor Grill |     1
Painting      |     8
Tent          |     4
Vase          |     9
Television    |     0
(6 rows)
*/

SELECT name, (SELECT count(id) FROM bids WHERE bids.item_id = items.id)
FROM items;

-- Trying to do this without scalar subqueries for extra practice
-- Also ended up being the further exploration :D
SELECT items.name, count(bids.id)
FROM items
LEFT JOIN bids ON bids.item_id = items.id
GROUP BY items.name;

/* We want to check that a given item is in our database. 
There is one problem though: we have all of the data for the item, but we don't know the id number. 
Write an SQL query that will display the id for the item that matches all of the data that we know, 
but does not use the AND keyword. Here is the data we know:

'Painting', 100.00, 250.00
*/

SELECT id
FROM items
WHERE (name, initial_price, sales_price) = ('Painting', 100.00, 250.00);

-- Solution uses the row keyword as follows:
SELECT id
FROM items
WHERE ROW(name, initial_price, sales_price) = ROW('Painting', 100.00, 250.00);

/* Use EXPLAIN to check the efficiency of the query statement we used in the exercise on EXISTS:

SELECT name FROM bidders
WHERE EXISTS (SELECT 1 FROM bids WHERE bids.bidder_id = bidders.id);

First use just EXPLAIN, then include the ANALYZE option as well. For your answer, list any SQL statements you used, 
along with the output you get back, and your thoughts on what is happening in both cases.
*/

EXPLAIN SELECT name FROM bidders
WHERE EXISTS (SELECT 1 FROM bids WHERE bids.bidder_id = bidders.id);

EXPLAIN ANALYZE SELECT name FROM bidders
WHERE EXISTS (SELECT 1 FROM bids WHERE bids.bidder_id = bidders.id);

/* Run EXPLAIN ANALYZE on the two statements above. Compare the planning time, execution time, and the 
total time required to run these two statements. Also compare the total "costs". Which statement is more efficient and why?

SELECT MAX(bid_counts.count) FROM
  (SELECT COUNT(bidder_id) FROM bids GROUP BY bidder_id) AS bid_counts;

SELECT COUNT(bidder_id) AS max_bid FROM bids
  GROUP BY bidder_id
  ORDER BY max_bid DESC
  LIMIT 1;
*/

EXPLAIN ANALYZE SELECT MAX(bid_counts.count) FROM
  (SELECT COUNT(bidder_id) FROM bids GROUP BY bidder_id) AS bid_counts;

EXPLAIN ANALYZE SELECT COUNT(bidder_id) AS max_bid FROM bids
  GROUP BY bidder_id
  ORDER BY max_bid DESC
  LIMIT 1;

/*
For the first: planning time = 0.137 ms, execution time = 0.088ms, total cost = 37.16
For the second: planning time = 0.203 ms, execution time = 0.104ms, total cost = 35.65

So the subquery is faster but slightly more costly.



*/